package marketsim.orderbook

import marketsim.{LimitOrder, MarketOrder}

class Queue[T <: Entry] {

    private val heap = new ChunkDeque[T]()

    def insert(order : T) = heap insert order

    /**
     * Matches other market order against order queue
     * @return unmatched volume of the other order
     */
    def matchWith(other : MarketOrder) =
    {
        def inner(unmatched : Int) : Int =
        {
            if (heap.isEmpty || unmatched == 0)
                unmatched
            else {
                val mine = heap.top
                assert(other.side != mine.side)
                val trade_volume = mine.getVolumeUnmatched min unmatched
                val trade_price = mine.order.price
                heap takeVolumeFromTop trade_volume

                mine.order OnTraded (trade_price, trade_volume)
                other      OnTraded (trade_price, trade_volume)

                if (mine.isEmpty) {
                    mine.order.OnMatched()
                    heap.pop()
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
            if (heap.isEmpty || unmatched == 0)
                unmatched
            else {
                val mine = heap.top
                assert(other.side != mine.side)
                if (mine canMatchWith other)
                {
                    val trade_volume = mine.getVolumeUnmatched min unmatched
                    val trade_price = mine.order.price
                    heap takeVolumeFromTop trade_volume

                    mine.order OnTraded (trade_price, trade_volume)
                    other      OnTraded (trade_price, trade_volume)

                    if (mine.isEmpty) {
                        mine.order.OnMatched()
                        heap.pop()
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
