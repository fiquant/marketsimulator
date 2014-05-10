package marketsim.orderbook

import marketsim.MarketOrder

class Queue[T <: Entry] {

    private val heap = new ChunkDeque[T]()

    def insert(order : T) = heap insert order


    /**
     * Matches other order against order queue
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
                val trade_volume = mine.getVolumeUnmatched min unmatched
                val trade_price = mine.order.price
                heap takeVolumeFromTop trade_volume

                heap.top.order OnTraded (trade_price, trade_volume)
                other          OnTraded (trade_price, trade_volume)

                inner(unmatched - trade_volume)
            }
        }
        inner(other.volumeAbsolute)
    }
}
