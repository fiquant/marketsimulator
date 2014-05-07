package marketsim.orderbook

import scala.collection.immutable.Queue

class ChunkDeque[T <: Entry](chunkSize : Int = 10) {

    type Chunk = Array[Queue[T]]

    private var chunks = Array.empty[Chunk]

    // index of the first allocated chunk
    private var base   = -1

    // index in chunk of the best order queue
    private var topIdx = Int.MaxValue

    def insert(x : T)
    {
        val key = x.signedTicks
        val chunkIdx = if (key > 0) key / chunkSize else key / chunkSize - 1

        if (chunks.isEmpty) {
            chunks = new Array[Chunk](1)
            base = chunkIdx
        } else {
            if (chunkIdx < base) {
                chunks = new Array[Chunk](base - chunkIdx) ++ chunks
                base = chunkIdx
            } else if (chunkIdx > base + chunks.length - 1) {
                chunks = chunks ++ new Array[Chunk](chunkIdx - base - chunks.length + 1)
            }
        }

        if (chunks(chunkIdx - base) == null)
            chunks(chunkIdx - base) = new Chunk(chunkSize)

        val relIdx =   key - chunkIdx * chunkSize

        val myChunk = chunks(chunkIdx - base)


        myChunk(relIdx) = if (myChunk(relIdx) == null) Queue[T](x) else myChunk(relIdx) enqueue x

        if (key < topIdx)
            topIdx = key
    }

    def top = {
        assert(chunks.nonEmpty)
        chunks(0)(topIdx - base*chunkSize).front
    }

}
