package marketsim.orderbook

import marketsim._
import marketsim.MarketOrder
import marketsim.LimitOrder

class Local(processingTime : Time = 0.0) extends OrderbookDispatch {

    val Asks = new Queue[SellEntry]
    val Bids = new Queue[BuyEntry]

    override def toString = "{asks = " + Asks + "; " + "bids = " + Bids + "}"

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
                order OnStopped (Bids matchWith (order, order.owner))
            case Buy =>
                order OnStopped (Asks matchWith (order, order.owner))
        }

    def process(order : LimitOrder) =

        order.side match {
            case Sell =>
                Asks insert SellEntry(order, Bids matchWith (order, order.owner))
            case Buy =>
                Bids insert BuyEntry(order, Asks matchWith (order, order.owner))
        }

    def process(cancel : CancelOrder) =

        cancel.order.side match {
            case Sell => Asks cancel cancel.order
            case Buy  => Bids cancel cancel.order
        }
}
