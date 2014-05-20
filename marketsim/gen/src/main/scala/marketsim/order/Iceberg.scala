package marketsim.order

import marketsim._
import marketsim.OrderRequest

object Iceberg
{
    case class Order(proto : PriceOrder, lotSize : () => Int) extends PriceOrder
    {
        self =>

        class State(target : OrderbookDispatch, events : OrderListener) extends OrderListener
        {
            var volumeUnnmatched = proto.volume

            def OnTraded(o : marketsim.Order, price : Ticks, volume : Int)
            {
                volumeUnnmatched += volume
                events OnTraded (self, price, volume)
            }

            private def newOrder() =
            {
                val lot = lotSize()
                assert(lot > 0)
                if (volumeUnnmatched > 0)
                    proto withVolume ( lot min volumeUnnmatched)
                else
                    proto withVolume (-lot max volumeUnnmatched)
            }

            private def newOrderSent() =
            {
                val o = newOrder()
                target handle OrderRequest(o, this)
                o
            }

            def OnStopped(o : marketsim.Order, unmatched : Int)
            {
                if (unmatched == 0 && volumeUnnmatched != 0) {
                    order = newOrderSent()
                } else
                    events OnStopped (self, volumeUnnmatched)
            }

            def cancel()
            {
                target handle CancelOrder(order)
            }

            var order = newOrderSent()
        }

        var state = Option.empty[State]

        private def getOrder = if (state.isEmpty) proto else state.get.order withVolume state.get.volumeUnnmatched

        def volume = getOrder.volume
        def price = getOrder.price
        def withVolume(v : Int) = copy(proto = getOrder withVolume v)
        def withPrice(p : Ticks) = copy(proto = getOrder withPrice p)

        def processIn(target : OrderbookDispatch, events : OrderListener)
        {
            if (proto.volume != 0) {
                state = Some (new State(target, events))
            }
        }

        override def cancel()
        {
            if (state.nonEmpty)
                state.get.cancel()
        }

        override def toString = s"Iceberg($proto, $lotSize)"
    }

    case class Factory(proto : PriceOrderFactory, lotSize : () => Int) extends PriceOrderFactory
    {
        def create = new Order(proto.create, lotSize)
    }

}
