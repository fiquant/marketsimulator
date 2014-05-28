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
                    var stopOrder = Option.empty[marketsim.Order]

                    var cancelled = false
                    var handler = Option.empty[(Ticks, () => Unit)]

                    def flush()
                    {
                        if (!cancelled) {
                            target handle CancelOrder(proto)
                            stopOrder = Some(MarketOrder(-volumeMatched))
                            target handle OrderRequest(stopOrder.get, this)
                            cancel_ = () => {
                                target handle CancelOrder(stopOrder.get)
                                bestPriceChanged -= handler.get
                            }
                        }
                    }

                    val bestPriceChanged = proto.side match {
                        case Buy => OnceLessThan(orderbook.BestPrice(target.Bids))
                        case Sell  => OnceGreaterThan(orderbook.BestPrice(target.Asks))
                    }

                    def volumeMatched = proto.volume - volumeUnmatched
                    def perSharePrice = (priceTraded / volumeMatched).abs

                    def OnTraded(o : marketsim.Order, price : Ticks, volume : Int)
                    {
                        volumeUnmatched += volume

                        if (volumeMatched != 0 && priceTraded != price && Some(o) != stopOrder)
                        {
                            if (handler.nonEmpty)
                                bestPriceChanged -= handler.get

                            val trigger = o.side match {
                                case Buy => perSharePrice * (1 - lossFactor)
                                case Sell => perSharePrice / (1 - lossFactor)
                            }

                            handler = Some((trigger.toInt, flush))

                            bestPriceChanged += handler.get
                        }
                        priceTraded += price

                        events OnTraded (self, price, volume)
                    }

                    def OnStopped(o : marketsim.Order, unmatched : Int)
                    {
                        self.cancel_ = () => ()

                        if (Some(o) == stopOrder)
                            events OnStopped (self, volumeUnmatched)
                    }

                    target handle OrderRequest(proto, this)

                    self.cancel_ = () => {
                        target handle CancelOrder(proto)
                        cancelled = true
                    }
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
