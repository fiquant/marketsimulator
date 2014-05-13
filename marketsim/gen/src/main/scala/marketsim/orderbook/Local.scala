package marketsim.orderbook

import marketsim._
import marketsim.MarketOrder
import marketsim.LimitOrder

class Local(processingTime : Time = 0.0) extends Orderbook {

    private val asks = new Queue[SellEntry]
    private val bids = new Queue[BuyEntry]

    def Asks : IOrderQueue = asks
    def Bids : IOrderQueue = bids

    override def toString = "{asks = " + asks + "; " + "bids = " + bids + "}"

    private val requests = collection.mutable.Queue[Request]()

    import marketsim.Scheduler.scheduleAfter

    private def wakeUp() {
        requests.dequeue() processIn this
        if (requests.nonEmpty)
            scheduleAfter(processingTime, { wakeUp() })
    }

    def handle(request : Request) = {
        requests enqueue request
        if (requests.length == 1)
            scheduleAfter(processingTime, { wakeUp() })
    }

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
                asks insert SellEntry(order, bids matchWith order)
            case Buy =>
                bids insert BuyEntry(order, asks matchWith order)
        }
}
