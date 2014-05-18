import marketsim._

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
}
