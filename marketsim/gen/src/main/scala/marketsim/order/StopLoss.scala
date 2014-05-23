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
                target handle OrderRequest(proto, events proxy this)
            }

            proto.side match {
                case Sell => OnceLessThan(orderbook.BestPrice(target.Asks)) += (trigger, flush())
                case Buy  => OnceGreaterThan(orderbook.BestPrice(target.Bids)) += (trigger, flush())
            }
        }

        def volume = proto.volume // in fact it is not correct. should we keep track of unmatched volume?
        def withVolume(v : Int) = proto withVolume v
    }

}
