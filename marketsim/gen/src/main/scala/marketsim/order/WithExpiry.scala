package marketsim.order

import marketsim._
import marketsim.OrderRequest

object WithExpiry
{
    class Order(proto : OrderFactory, expiration : () => Time) extends marketsim.Order
    {
        def processIn(target : OrderbookDispatch, events : OrderListener)
        {
            val order = proto.create
            target handle OrderRequest(order, events proxy this)

            import marketsim.Scheduler.scheduleAfter

            scheduleAfter(expiration(), target handle CancelOrder(order))
        }

        override def toString = s"WithExpiry($proto, $expiration)"
    }

    case class Factory(proto : OrderFactory, expiration : () => Time) extends OrderFactory
    {
        def create = new Order(proto, expiration)
    }

}

