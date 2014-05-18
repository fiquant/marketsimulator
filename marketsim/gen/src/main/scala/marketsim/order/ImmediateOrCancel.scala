package marketsim.order

import marketsim._
import marketsim.OrderRequest

object ImmediateOrCancel
{
    class Order(proto : marketsim.Order) extends marketsim.Order
    {
        val volume = proto.volume

        def processIn(target : OrderbookDispatch, events : OrderListener)
        {
            target handle OrderRequest(proto, events)
            target handle CancelOrder(proto)
        }
    }

    class Factory(proto : OrderFactory) extends OrderFactory
    {
        def create = new Order(proto.create)
    }

}

