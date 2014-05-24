package marketsim.order

import marketsim._

object StopLoss
{
    case class Order(proto : marketsim.Order, trigger : Ticks) extends marketsim.Order
    {
        def processIn(target : OrderbookDispatch, events : OrderListener)
        {
            def flush()
            {
                if (!cancelled) {
                    target handle OrderRequest(proto, events proxy this)
                    cancel_ = () => target handle CancelOrder(proto)
                }
            }

            proto.side match {
                case Sell => OnceLessThan(orderbook.BestPrice(target.Asks)) += (trigger, flush())
                case Buy  => OnceGreaterThan(orderbook.BestPrice(target.Bids)) += (trigger, flush())
            }
        }

        private var cancel_ = () => ()
        private var cancelled = false

        override def cancel() {
            cancelled = true
            cancel_()
        }


        def volume = proto.volume
        def withVolume(v : Int) = proto withVolume v

        override def toString = s"StopLoss($proto, $trigger)"
    }
}
