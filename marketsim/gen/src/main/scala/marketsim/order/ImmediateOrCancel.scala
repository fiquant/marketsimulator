package marketsim.order

import marketsim._
import marketsim.OrderRequest

object ImmediateOrCancel
{
    class Order(proto : OrderFactory) extends marketsim.Order
    {
        self =>
        def processIn(target : OrderbookDispatch, events : OrderListener)
        {
            val order = proto.create
            target handle OrderRequest(order, events proxy this)
            target handle CancelOrder(order)
        }

        override def toString = s"IoC($proto)"
    }

    case class Factory(proto : OrderFactory) extends OrderFactory
    {
        def create = new Order(proto)
    }

}

