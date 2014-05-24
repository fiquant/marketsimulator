package marketsim.order

import marketsim._

object FloatingPrice
{
    case class Order(proto : PriceOrder, floatingPrice : Observable[Ticks]) extends PriceOrder
    {
        self =>

        def volume = proto.volume
        def price  = proto.price

        def withVolume(v : Int) = copy(proto = proto withVolume v)
        def withPrice(p : Ticks) = copy(proto = proto withPrice p)

        override def toString = s"FloatingPrice($proto, $floatingPrice)"

        def processIn(target : OrderbookDispatch, events : OrderListener)
        {
            var order = Option.empty[PriceOrder]
            var unmatched = volume

            val listener = new OrderListener
            {
                def OnTraded(o : marketsim.Order, price : Ticks, volume : Volume) = {
                    unmatched += volume
                    events OnTraded (self, price, volume)
                }

                def OnStopped(o : marketsim.Order, unmatchedVolume : Volume) = {
                    if (unmatched == 0) {
                        order = None
                        events OnStopped (self, unmatchedVolume)
                    }
                }
            }

            def resend()
            {
                if (order.nonEmpty) {
                    target handle CancelOrder(order.get)
                    order = None
                }

                import marketsim.Scheduler.async

                async {
                    if (unmatched != 0) {
                        floatingPrice.value match {
                            case Some(newPrice) =>
                                order = Some(proto withPrice newPrice withVolume unmatched)
                                target handle OrderRequest(order.get, listener)
                            case None =>
                        }
                    }
                }
            }

            resend()

            floatingPrice += { _ => resend() }
        }
    }

    case class Factory(proto : PriceOrderFactory, floatingPrice : Observable[Ticks]) extends PriceOrderFactory
    {
        def create = Order(proto.create, floatingPrice)
    }
}
