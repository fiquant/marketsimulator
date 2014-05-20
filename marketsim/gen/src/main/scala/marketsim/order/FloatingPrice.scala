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

        class State(target : OrderbookDispatch, events : OrderListener) extends OrderListener
        {
            var order = Option.empty[PriceOrder]

            def resend()
            {
                if (order.nonEmpty) {
                    target handle CancelOrder(order.get)
                    order = None
                }

                import marketsim.Scheduler.async

                async {
                    floatingPrice.value match {
                        case Some(newPrice) =>
                            order = Some(order.get withPrice newPrice)
                            target handle OrderRequest(order.get, this)
                        case None =>
                    }
                }
            }

            resend()

            def OnTraded(o : marketsim.Order, price : Ticks, volume : Volume) = events OnTraded (self, price, volume)

            def OnStopped(o : marketsim.Order, unmatchedVolume : Volume) = {
                order = None
                events OnStopped (self, unmatchedVolume)
            }

        }

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
