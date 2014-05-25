package marketsim.order

import marketsim._
import marketsim.OrderRequest

object WithExpiry
{
    case class Order(proto : PriceOrder, expiration : () => Time) extends PriceMetaOrder
    {
        def process(target : Orderbook, events : OrderListener)
        {
            target handle OrderRequest(proto, events proxy this)

            import marketsim.Scheduler.scheduleAfter

            cancel_ = () => target handle CancelOrder(proto)

            scheduleAfter(expiration(), cancel())
        }

        def withVolume(v : Int) = copy(proto = proto withVolume v)
        def withPrice(p : Ticks) = copy(proto = proto withPrice p)

        override def toString = s"WithExpiry($proto, $expiration)"
    }

    case class Factory(proto : PriceOrderFactory, expiration : () => Time) extends OrderFactory
    {
        def create = new Order(proto.create, expiration)
    }

}

