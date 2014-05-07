package marketsim.orderbook

import scala.collection.mutable

class ChunkDeque[T <: Entry](chunkSize : Int = 10) {

    type Chunk = Array[mutable.Queue[T]]

    private var chunks = Array.empty[Chunk]

    // index of the first allocated chunk
    private var base   = -1

    // index in chunk of the best order queue
    private var topIdx = -1

    def insert(x : T)
    {
        val key = x.signedTicks
        val chunkIdx = if (key > 0) key / chunkSize else key / chunkSize - 1
        val relIdx =   key - chunkIdx * chunkSize

        if (chunks.isEmpty) {
            chunks = new Array[Chunk](1)
            base = chunkIdx
            chunks(0) = new Chunk(chunkSize)
            val q = new mutable.Queue[T]()
            q enqueue x
            chunks(0)(relIdx) = q
            topIdx = key
        }
    }

    def top = {
        assert(chunks.nonEmpty)
        chunks(0)(topIdx - base*chunkSize).front
    }

}
