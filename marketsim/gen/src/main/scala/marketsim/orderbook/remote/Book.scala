package marketsim.orderbook.remote

import marketsim._

class Book(target : Orderbook, link : TwoWayLink) extends Orderbook {

    class Queue(target : OrderQueue) extends OrderQueue
    {
        val BestPossiblyChanged = new Event[Option[PriceVolume]]
        val TradeDone = new Event[PriceVolume]

        target.BestPossiblyChanged += (price => link.down send BestPossiblyChanged(price))
        target.TradeDone           += (trade => link.down send TradeDone(trade))
    }

    val Asks = new Queue(target.Asks)
    val Bids = new Queue(target.Bids)

    def canHandle(order : MetaOrder) = target canHandle order
    
    def handle(request : Request) = request match {
        case OrderRequest(o : MetaOrder, e) if !canHandle(o) =>
            o process (this, e)
        case _ =>
            link.up send {target handle (request remote link.down)}
    }

    override def toString = s"Remote($target)"

}
