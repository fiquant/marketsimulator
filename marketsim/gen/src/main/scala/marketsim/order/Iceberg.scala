package marketsim.order

import marketsim._
import marketsim.OrderRequest

object Iceberg
{
    case class Order(proto : PriceOrder, lotSize : () => Int) extends PriceMetaOrder
    {
        self =>

        def withVolume(v : Int) = copy(proto = proto withVolume v)
        def withPrice(p : Ticks) = copy(proto = proto withPrice p)

        def process(target : Orderbook, events : OrderListener)
        {
            if (proto.volume != 0) {
                class State extends OrderListener
                {
                    var volumeUnmatched = proto.volume

                    def OnTraded(o : marketsim.Order, price : Ticks, volume : Int)
                    {
                        volumeUnmatched += volume
                        events OnTraded (self, price, volume)
                    }

                    private def newOrder() =
                    {
                        val lot = lotSize()
                        assert(lot > 0)
                        if (volumeUnmatched > 0)
                            proto withVolume ( lot min volumeUnmatched)
                        else
                            proto withVolume (-lot max volumeUnmatched)
                    }

                    private def newOrderSent() =
                    {
                        val o = newOrder()
                        target handle OrderRequest(o, this)
                        o
                    }

                    def OnStopped(o : marketsim.Order, unmatched : Int)
                    {
                        if (unmatched == 0 && volumeUnmatched != 0) {
                            order = newOrderSent()
                        } else
                            events OnStopped (self, volumeUnmatched)
                    }

                    self.cancel_ = () =>
                        target handle CancelOrder(order)

                    var order = newOrderSent()
                }

                new State
            }
        }

        override def toString = s"Iceberg($proto, $lotSize)"
    }

    case class Factory(proto : PriceOrderFactory, lotSize : () => Int) extends PriceOrderFactory
    {
        def create = new Order(proto.create, lotSize)
    }

}
