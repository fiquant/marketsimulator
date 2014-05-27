package marketsim.order

import marketsim._
import marketsim.OrderRequest

object WithStopLoss
{
    case class Order(proto : marketsim.Order, lossFactor : Float) extends MetaOrder
    {
        self =>

        def withVolume(v : Int) = copy(proto = proto withVolume v)

        def process(target : Orderbook, events : OrderListener)
        {
            if (proto.volume != 0) {
                class State extends OrderListener
                {
                    var volumeUnmatched = proto.volume
                    var priceTraded = 0
                    var stopOrder = Option.empty[StopLoss.Order]

                    val source = proto.side match {
                        case Sell => OnceGreaterThan(orderbook.BestPrice(target.Bids))
                        case Buy  => OnceLessThan(orderbook.BestPrice(target.Asks))
                    }
                    
                    def volumeMatched = proto.volume - volumeUnmatched
                    def perSharePrice = (priceTraded / volumeMatched).abs

                    def OnTraded(o : marketsim.Order, price : Ticks, volume : Int)
                    {
                        volumeUnmatched += volume
                        priceTraded += price

                        if (volumeMatched != 0)
                        {
                            if (stopOrder.nonEmpty)
                                target handle CancelOrder(stopOrder.get)

                            val trigger = o.side match {
                                case Buy => perSharePrice * (1 - lossFactor)
                                case Sell => perSharePrice / (1 - lossFactor)
                            }

                            stopOrder = Some(StopLoss.Order(MarketOrder(-volumeMatched), trigger.toInt))

                            target handle OrderRequest(stopOrder.get, events proxy self)
                        }

                        events OnTraded (self, price, volume)
                    }

                    def OnStopped(o : marketsim.Order, unmatched : Int)
                    {
                        self.cancel_ = () => ()
                    }

                    target handle OrderRequest(proto, this)

                    self.cancel_ = () =>
                        target handle CancelOrder(proto)
                }

                new State
            }
        }

        override def toString = s"WithStopLoss($proto, $lossFactor)"
    }

    case class Factory(proto : OrderFactory, lossFactor : () => Float) extends OrderFactory
    {
        def create = new Order(proto.create, lossFactor())
    }

}
