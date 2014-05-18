import marketsim._
import marketsim.Scheduler._

package object test
{
    case class OrderEvents(trace : String => Unit, name : String) extends OrderListener
    {
        def OnTraded(order : Order, price : Ticks, volume : Volume)
        {
            trace(s"$order traded at $price with $volume")
        }

        def OnStopped(order : Order, unmatchedVolume : Volume)
        {
            trace(order + (if (unmatchedVolume != 0) " canceled" else " matched completely"))
        }

        override def toString = name
    }

    def withLogging(trace : String => Unit)(book : Orderbook) =
    {
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

        book
    }

    class LoggedAccount(trace_ : String => Unit, book : Orderbook, name : String)
    {
        val account = new marketsim.Account(book)

        def trace(s : String) = trace_(s"$name : $s")

        account.OrderSent += { order => trace(s"sending $order") }
        account.OrderTraded += { case (order, price, volume)  =>
            trace(s"$order traded $volume at $price")
            trace(s"position = ${account.getPosition}; balance = ${account.getBalance}")
        }
        account.OrderStopped += { case (order, unmatched) =>
            trace(order + (if (unmatched == 0) " matched completely" else " unmatched volume: " + unmatched )) }

        val ordersSent = new PendingOrders(account)

        def sendOrder(factory : OrderFactory) {
            trace("before = " + book)
            val order = factory.create
            account send order
            async {
                trace("after = " + book)
                trace("")
            }
        }

        def cancel(order : Order) {
            trace("cancelling " + order)
            account send CancelOrder(order)
        }


    }
}
