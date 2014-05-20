package marketsim.order

import marketsim._

object FloatingPrice
{
    case class Order(proto : PriceOrder, floatingPrice : Observable[Ticks]) extends PriceOrder
    {
        self =>

        private def getOrder : PriceOrder =
            if (state.nonEmpty && state.get.order.nonEmpty)
                state.get.order.get withVolume state.get.unmatched
            else
                proto

        def volume = getOrder.volume
        def price  = getOrder.price

        def withVolume(v : Int) = copy(proto = getOrder withVolume v)
        def withPrice(p : Ticks) = copy(proto = getOrder withPrice p)

        class State(target : OrderbookDispatch, events : OrderListener) extends OrderListener
        {
            var order = Option.empty[PriceOrder]
            var unmatched = volume

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
                                target handle OrderRequest(order.get, this)
                            case None =>
                        }
                    }
                }
            }

            resend()

            floatingPrice += { _ => resend() }

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

        override def toString = s"FloatingPrice($proto, $floatingPrice)"

        private var state = Option.empty[State]

        def processIn(target : OrderbookDispatch, events : OrderListener)
        {
            state = Some(new State(target, events))
        }
    }

    case class Factory(proto : PriceOrderFactory, floatingPrice : Observable[Ticks]) extends PriceOrderFactory
    {
        def create = Order(proto.create, floatingPrice)
    }
}
