package marketsim.order

import marketsim._
import marketsim.OrderRequest

object ImmediateOrCancel
{
    class Order(proto : marketsim.Order) extends marketsim.Order
    {
        def processIn(target : OrderbookDispatch, events : OrderListener)
        {
            target handle OrderRequest(proto, events proxy this)
            target handle CancelOrder(proto)
        }

        def withVolume(v : Int) = new Order(proto withVolume v)

        override def toString = s"IoC($proto)"
    }

    case class Factory(proto : OrderFactory) extends OrderFactory
    {
        def create = new Order(proto.create)
    }

}

