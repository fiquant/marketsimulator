import marketsim._

package object test
{
    case class OrderEvents[T](trace : String => Unit, name : String) extends OrderListener[T]
    {
        def OnTraded(order : T, price : Ticks, volume : Volume)
        {
            trace(s"$order traded at $price with $volume")
        }

        def OnStopped(order : T, unmatchedVolume : Volume)
        {
            trace(order + (if (unmatchedVolume != 0) " canceled" else " matched completely"))
        }

        override def toString = name
    }

}
