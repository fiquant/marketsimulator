package marketsim.orderbook

import marketsim._
import marketsim.MarketOrder
import marketsim.LimitOrder

class Local extends Orderbook {

    private val asks = new Queue[SellEntry]
    private val bids = new Queue[BuyEntry]

    def process(order : MarketOrder) =

        order.side match {
            case Sell =>
                order OnStopped (bids matchWith order)
            case Buy =>
                order OnStopped (asks matchWith order)
        }

    def process(order : LimitOrder) =

        order.side match {
            case Sell =>
                //asks insert new SellEntry(order, bids matchWith order)
            case Buy =>
                //order OnStopped (asks matchWith order)
        }
}
