package marketsim.orderbook

import marketsim._
import marketsim.MarketOrder
import marketsim.LimitOrder
import scala.Some

class Queue[T <: Entry] extends OrderQueue {

    private val orders = new ChunkDeque[T]()

    val BestPossiblyChanged = new Event[Option[Ticks]]
    val TradeDone = new Event[(Ticks, Int)]

    import marketsim.Scheduler.async

    private def notifyBestChanged()
    {
        async {
            BestPossiblyChanged(if (orders.isEmpty) None else Some(orders.top.order.price))
        }
    }

    def insert(order : T) {
        orders insert order
        if (order eq orders.top)
            notifyBestChanged()
    }

    def cancel(order : LimitOrder) =
        if (!orders.isEmpty) {
            val isTop = orders.top.order eq order
            val unmatched = orders cancel order
            if (unmatched > 0)
                order OnStopped unmatched
            if (isTop)
                notifyBestChanged()
        }

    override def toString = orders.toString

    /**
     * Matches other market order against order queue
     * @return unmatched volume of the other order
     */
    def matchWith(other : MarketOrder, otherEvents : OrderListener) =
    {
        def inner(unmatched : Int) : Int =
        {
            if (orders.isEmpty || unmatched == 0)
                unmatched
            else {
                val mine = orders.top
                assert(other.side != mine.side)

                val trade_volume = mine matchWith (other, unmatched, otherEvents)

                async {
                    TradeDone((mine.order.price, trade_volume))
                }

                orders takeVolumeFromTop trade_volume

                if (mine.isEmpty) {
                    async { mine.owner OnStopped (mine.order, 0) }
                    orders.pop()
                    inner(unmatched - trade_volume)
                }
                else
                    0
            }
        }
        val ret = inner(other.volumeAbsolute)
        if (ret == 0) async { otherEvents OnStopped (other, 0) }
        notifyBestChanged()
        ret
    }

    /**
     * Matches other market order against order queue
     * @return unmatched volume of the other order
     */
    def matchWith(other : LimitOrder, otherEvents : OrderListener) =
    {
        def inner(unmatched : Int) : Int =
        {
            if (orders.isEmpty || unmatched == 0)
                unmatched
            else {
                val mine = orders.top
                assert(other.side != mine.side)
                if (mine canMatchWith other)
                {
                    val trade_volume = mine matchWith (other, unmatched, otherEvents)

                    async {
                        TradeDone((mine.order.price, trade_volume))
                    }

                    orders takeVolumeFromTop trade_volume

                    if (mine.isEmpty) {
                        async { mine.owner OnStopped (mine.order, 0) }
                        orders.pop()
                        inner(unmatched - trade_volume)
                    }
                    else
                        0
                }
                else
                    unmatched
            }
        }
        val ret = inner(other.volumeAbsolute)
        notifyBestChanged()
        if (ret == 0) async { otherEvents OnStopped (other, 0) }
        ret
    }
}
