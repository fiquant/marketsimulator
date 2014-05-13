package marketsim.orderbook.remote

import marketsim._

class Book(target : Orderbook, link : TwoWayLink) extends Orderbook {

    class Queue(target : OrderQueue) extends OrderQueue
    {
        val BestPossiblyChanged = new Event[Option[Ticks]]
        val TradeDone = new Event[(Ticks, Int)]

        target.BestPossiblyChanged += (price => link.up send (() => BestPossiblyChanged(price)))
        target.TradeDone           += (trade => link.up send (() => TradeDone(trade)))
    }

    val Asks = new Queue(target.Asks)
    val Bids = new Queue(target.Bids)
    
    def handle(request : Request) =
        link.up send (() => target handle (request remote link.down))

}
