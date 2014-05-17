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

}
