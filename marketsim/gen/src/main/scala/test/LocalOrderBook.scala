package test

import marketsim._
import marketsim.Scheduler._
import scala.collection.immutable.Queue

case object LocalOrderBook extends Test {

    def apply(trace : String => Unit)
    {
        marketsim.Scheduler.create { scheduler =>

            val book = new marketsim.orderbook.Local
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

            var ordersSent = Queue.empty[LimitOrder]

            def sendLimit(factory : LimitOrderFactory) {
                trace("before = " + book)
                val order = factory.create
                account send order
                ordersSent = ordersSent enqueue order
                async {
                    trace("after = " + book)
                    trace("")
                }
            }

            val sellOrders = LimitOrderFactory(() => 100 + currentTime.toInt, () => 1)
            val buyOrders = LimitOrderFactory(() => 95 + currentTime.toInt, () => -2)

            0 to 4 foreach { i => schedule(i, sendLimit(sellOrders)) }
            0 to 4 foreach { i => schedule(i + 5, sendLimit(buyOrders)) }

            def cancel(order : LimitOrder) {
                trace("cancelling " + order)
                account send CancelOrder(order)
            }

            schedule(10, {
                ordersSent foreach cancel
            })


            scheduler workTill 50
        }
    }
}