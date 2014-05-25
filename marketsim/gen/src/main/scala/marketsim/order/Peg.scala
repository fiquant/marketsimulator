package marketsim.order

import marketsim._
import marketsim.OrderbookDispatch
import marketsim.OrderListener
import marketsim.CancelOrder
import marketsim.OrderRequest
import marketsim.PriceOrderFactory

object Peg
{
    case class Order(proto : PriceOrder) extends PriceMetaOrder
    {
        self =>

        def withVolume(v : Int) = copy(proto = proto withVolume v)
        def withPrice(p : Ticks) = copy(proto = proto withPrice p)

        override def toString = s"Peg($proto)"

        def processIn(target : OrderbookDispatch, events : OrderListener)
        {
            var order = Option.empty[PriceOrder]

            var unmatched = volume
            var cancelled = false

            def alive = unmatched != 0 && !cancelled

            val listener = new OrderListener {
                def OnTraded(o : marketsim.Order, price : Ticks, volume : Volume) = {
                    unmatched += volume
                    events OnTraded (self, price, volume)
                }

                def OnStopped(o : marketsim.Order, unmatchedVolume : Volume) = {
                    if (!alive) {
                        order = None
                        events OnStopped (self, unmatchedVolume)
                    }
                }
            }

            val floatingPriceVolume = proto.side match {
                case Sell => orderbook.BestPriceVolume(target.Asks)
                case Buy  => orderbook.BestPriceVolume(target.Bids)
            }

            def resend()
            {
                if (floatingPriceVolume.value match {
                    case Some((newPrice, newVolume)) =>
                        order match {
                            case None => true
                            case Some(o) if o.side == Sell =>
                                o.price > newPrice || o.price == newPrice && unmatched < newVolume
                            case Some(o) if o.side == Buy =>
                                o.price < newPrice || o.price == newPrice && unmatched < newVolume
                        }
                    case None =>
                        order.nonEmpty
                }) {
                    if (order.nonEmpty) {
                        target handle CancelOrder(order.get)
                        order = None
                    }

                    import marketsim.Scheduler.async

                    async {
                        if (alive) {
                            floatingPriceVolume.value match {
                                case Some((newPrice, newVolume)) =>
                                    val delta = unmatched.signum
                                    order = Some(proto withPrice (newPrice - delta) withVolume unmatched)
                                    target handle OrderRequest(order.get, listener)
                                case None =>
                            }
                        }
                    }
                }

            }

            cancel_ = () => {
                    cancelled = true
                    resend()
            }

            resend()

            floatingPriceVolume += { _ => resend() }
        }
    }

    case class Factory(proto : PriceOrderFactory) extends PriceOrderFactory
    {
        def create = Order(proto.create)
    }
}
