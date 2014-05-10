package marketsim.orderbook

import marketsim.{LimitOrder, MarketOrder}

class Queue[T <: Entry] {

    private val orders = new ChunkDeque[T]()

    def insert(order : T) = orders insert order

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
                    mine.order.OnMatched()
                    orders.pop()
                    inner(unmatched - trade_volume)
                }
                else
                    0
            }
        }
        inner(other.volumeAbsolute)
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
                        mine.order.OnMatched()
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
        inner(other.volumeAbsolute)
    }
}
