package marketsim.order

import marketsim._
import marketsim.OrderRequest

object Iceberg
{
    class Order(proto : marketsim.Order, lotSize : () => Int) extends marketsim.Order
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

        def withVolume(v : Int) = this
        val volume = proto.volume

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

    case class Factory(proto : OrderFactory, lotSize : () => Int) extends OrderFactory
    {
        def create = new Order(proto.create, lotSize)
    }

}
