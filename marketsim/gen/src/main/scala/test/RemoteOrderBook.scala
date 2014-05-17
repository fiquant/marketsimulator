package test

import marketsim._
import marketsim.Scheduler._

case object RemoteOrderBook extends Test {

    def apply(trace_ : String => Unit)
    {
        def trace(s : String) = trace_(f"[$eventId% 4d]  $currentTime%2.1f\t$s%s")

        marketsim.Scheduler.create { scheduler =>

            val local = new marketsim.orderbook.Local
            val link = new marketsim.orderbook.remote.TwoWayLink(() => 0.2, () => 0.3)
            val book = new marketsim.orderbook.remote.Book(local, link)

            val account = new marketsim.Account(book)

            def OnBestChanged(sender : String, pv : Option[Ticks])
            {
                trace(s"best of $sender changed = " + pv)
            }

            def OnTraded(sender : String, pv : (Ticks, Int))
            {
                trace(sender + " on_traded: " + pv)
            }

            book.Asks.BestPossiblyChanged += { OnBestChanged("asks", _) }
            book.Bids.BestPossiblyChanged += { OnBestChanged("bids", _) }

            book.Asks.TradeDone += { OnTraded("asks", _) }
            book.Bids.TradeDone += { OnTraded("bids", _) }

            account.OrderSent += { order => trace("Sending " + order) }
            account.OrderTraded += { case (order, price, volume)  => trace(s"$order traded $volume at $price") }
            account.OrderStopped += { case (order, unmatched) =>
                trace(order + (if (unmatched == 0) " matched completely" else " unmatched volume: " + unmatched )) }

            def sendLimit(price : Ticks, volume : Int) {
                val order = LimitOrder(price, volume, account)
                trace("before = " + book)
                account send order
                async {
                    trace("after = " + book)
                    trace("")
                }
            }

            0 to 4 foreach { i => schedule(i, sendLimit(100 + i, 1)) }
            0 to 4 foreach { i => schedule(i + 5, sendLimit(100 + i, -2)) }

            scheduler workTill 50
        }
    }
}
