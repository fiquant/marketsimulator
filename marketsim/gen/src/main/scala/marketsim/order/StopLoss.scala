package marketsim.order

import marketsim._

object StopLoss
{
    case class Order(proto : marketsim.Order, trigger : Ticks) extends MetaOrder
    {
        self =>

        def process(target : Orderbook, events : OrderListener)
        {
            class State extends OrderListener
            {
                def OnTraded(order : marketsim.Order, price: Ticks, volume : Volume) = events OnTraded (self, price, volume)
                def OnStopped(order : marketsim.Order, unmatchedVolume : Volume) =
                    events OnStopped (self, unmatchedVolume)

                def flush()
                {
                    if (!cancelled) {
                        target handle OrderRequest(proto, this)
                        cancel_ = () => {
                            target handle CancelOrder(proto)
                            bestPriceChanged -= handler
                        }
                    }
                }

                val handler = (trigger, () => flush())

                val bestPriceChanged = proto.side match {
                    case Sell => OnceLessThan(orderbook.BestPrice(target.Bids))
                    case Buy  => OnceGreaterThan(orderbook.BestPrice(target.Asks))
                }

                bestPriceChanged += handler
            }

            new State
        }

        private var cancelled = false

        override def cancelImpl() {
            cancelled = true
        }

        def withVolume(v : Int) = copy(proto = proto withVolume v)

        override def toString = s"StopLoss($proto, $trigger)"
    }

    case class Factory(proto : OrderFactory, trigger : () => Ticks) extends OrderFactory
    {
        def create = Order(proto.create, trigger())
    }
}
