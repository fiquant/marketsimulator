package marketsim.orderbook

import marketsim._
import marketsim.MarketOrder
import marketsim.LimitOrder

class Local(acceptedOrders : MetaOrder => Boolean = _ => false,
            processingTime : Time = 0.0,
            val tickSize   : Double = 0.01) extends OrderbookDispatch {

    val Asks = new Queue[SellEntry]
    val Bids = new Queue[BuyEntry]

    override def toString = "{asks = " + Asks + "; " + "bids = " + Bids + "}"

    private val requests = collection.mutable.Queue[Request]()

    def canHandle(order : MetaOrder) = acceptedOrders(order)

    import marketsim.Scheduler.scheduleAfter

    private def wakeUp() {
        if (requests.nonEmpty) {
            requests.dequeue() processIn this
            if (requests.nonEmpty)
                scheduleAfter(processingTime, { wakeUp() })
        }
    }

    def handle(request : Request) = {
        requests enqueue request
        if (requests.length == 1)
            scheduleAfter(processingTime, { wakeUp() })
    }

    import marketsim.Scheduler.async

    def process(order : MarketOrder, events : OrderListener) =
    {
        order.side match {
            case Sell =>
                val unmatched = Bids matchWith (order, events)
                async { events OnStopped (order, unmatched) }

            case Buy =>
                val unmatched = Asks matchWith (order, events)
                async { events OnStopped (order, -unmatched) }

        }
    }

    def process(order : LimitOrder, events : OrderListener) =
    {
        order.side match {
            case Sell =>
                val unmatched = Bids matchWith (order, events)
                if (unmatched != 0)
                    Asks insert SellEntry(order, unmatched, events)
                else
                    async { events OnStopped (order, 0) }
            case Buy =>
                val unmatched = Asks matchWith (order, events)
                if (unmatched != 0)
                    Bids insert BuyEntry(order, unmatched, events)
                else
                    async { events OnStopped (order, 0)}
        }
    }

    def cancel(order : LimitOrder) =

        order.side match {
            case Sell => Asks cancel order
            case Buy  => Bids cancel order
        }
}
