package marketsim.order

import marketsim._
import marketsim.OrderRequest

object WithExpiry
{
    case class Order(proto : marketsim.Order, expiration : () => Time) extends marketsim.Order
    {
        private var cancelOrder = Option.empty[() => Unit]

        def processIn(target : OrderbookDispatch, events : OrderListener)
        {
            target handle OrderRequest(proto, events proxy this)

            import marketsim.Scheduler.scheduleAfter

            cancelOrder = Some { () => target handle CancelOrder(proto) }

            scheduleAfter(expiration(), cancel())
        }

        val volume = proto.volume

        def withVolume(v : Int) = copy(proto = proto withVolume v)

        override def cancel() =
            if (cancelOrder.nonEmpty)
                cancelOrder.get()

        override def toString = s"WithExpiry($proto, $expiration)"
    }

    case class Factory(proto : OrderFactory, expiration : () => Time) extends OrderFactory
    {
        def create = new Order(proto.create, expiration)
    }

}

