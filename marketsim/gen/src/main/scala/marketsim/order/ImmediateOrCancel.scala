package marketsim.order

import marketsim._
import marketsim.OrderRequest

object ImmediateOrCancel
{
    case class Order(proto : marketsim.Order) extends MetaOrder
    {
        def processIn(target : OrderbookDispatch, events : OrderListener)
        {
            target handle OrderRequest(proto, events proxy this)
            target handle CancelOrder(proto)
        }

        def withVolume(v : Int) = copy(proto = proto withVolume v)

        override def toString = s"IoC($proto)"
    }

    case class Factory(proto : OrderFactory) extends OrderFactory
    {
        def create = new Order(proto.create)
    }

}

