package marketsim.order

import marketsim._
import marketsim.OrderRequest

object Iceberg
{
    class Order(proto : OrderFactoryByVolume, lotSize : () => Int) extends marketsim.Order
    {
        class State(target : OrderbookDispatch, events : OrderListener)
        {
            var volumeUnnmatched = -1

        }

        def withVolume(v : Int) = this

        def processIn(target : OrderbookDispatch, events : OrderListener)
        {
            val order = proto.create(lotSize())
            target handle OrderRequest(order, events proxy this)
        }

        override def toString = s"Iceberg($proto, $lotSize)"
    }

    case class Factory(proto : OrderFactoryByVolume, lotSize : () => Int) extends OrderFactory
    {
        def create = new Order(proto, lotSize)
    }

}
