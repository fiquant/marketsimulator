import marketsim._

package object test
{
    case class OrderEvents[T](trace : String => Unit, name : String) extends OrderListener[T]
    {
        def OnTraded(order : T, price : Ticks, volume : Volume)
        {
            trace(s"$order traded at $price with $volume")
        }

        def OnMatched(order : T)
        {
            trace(s"$order matched completely")
        }

        def OnCancelled(order : T)
        {
            trace(s"$order cancelled")
        }

        override def toString = name
    }

}
