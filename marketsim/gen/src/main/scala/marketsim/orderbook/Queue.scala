package marketsim.orderbook

import marketsim.{Ticks, Event, LimitOrder, MarketOrder}

class Queue[T <: Entry] {

    private val orders = new ChunkDeque[T]()

    val BestPossiblyChanged = new Event[Option[Ticks]]

    private def notifyBestChanged()
    {
        import marketsim.Scheduler._
        async {
            BestPossiblyChanged(if (orders.isEmpty) None else Some(orders.top.order.price))
        }
    }

    def insert(order : T) {
        orders insert order
        if (order eq orders.top)
            notifyBestChanged()
    }

    override def toString = orders.toString

    /**
     * Matches other market order against order queue
     * @return unmatched volume of the other order
     */
    def matchWith(other : MarketOrder) =
    {
        def inner(unmatched : Int) : Int =
        {
            if (orders.isEmpty || unmatched == 0)
                unmatched
            else {
                val mine = orders.top
                assert(other.side != mine.side)

                val trade_volume = mine matchWith (other, unmatched)

                orders takeVolumeFromTop trade_volume

                if (mine.isEmpty) {
                    mine.order OnStopped 0
                    orders.pop()
                    inner(unmatched - trade_volume)
                }
                else
                    0
            }
        }
        val ret = inner(other.volumeAbsolute)
        notifyBestChanged()
        ret
    }

    /**
     * Matches other market order against order queue
     * @return unmatched volume of the other order
     */
    def matchWith(other : LimitOrder) =
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
                    val trade_volume = mine matchWith (other, unmatched)

                    orders takeVolumeFromTop trade_volume

                    if (mine.isEmpty) {
                        mine.order OnStopped 0
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
        ret
    }
}
