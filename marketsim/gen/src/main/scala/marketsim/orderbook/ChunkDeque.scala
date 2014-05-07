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

        val myChunk = chunks(chunkIdx - base)

        val relIdx =   key - chunkIdx * chunkSize

        myChunk(relIdx) = if (myChunk(relIdx) == null) Queue[T](x) else myChunk(relIdx) enqueue x

        if (key < topIdx)
            topIdx = key
    }

    def top = {
        assert(chunks.nonEmpty)
        chunks(0)(topIdx - base*chunkSize).front
    }

    def isEmpty = chunks.isEmpty

    def pop() {
        assert(!isEmpty)
        val relIdx = topIdx - base*chunkSize
        val myChunk = chunks(0)
        myChunk(relIdx) = myChunk(relIdx).dequeue._2

        if (myChunk(relIdx).isEmpty)
        {
            myChunk(relIdx) = null

            val newTop = myChunk.indexWhere({ _ != null}, relIdx)

            if (newTop != -1) {
                topIdx += newTop - relIdx
            } else {
                chunks(0) = null
                val firstNonNull = chunks.indexWhere({ _ != null })
                if (firstNonNull == -1) {
                    chunks = Array.empty[Chunk]
                } else {
                    chunks = chunks.slice(firstNonNull, chunks.length )
                    base += firstNonNull
                    topIdx = (chunks(0) indexWhere { _ != null }) + base*chunkSize
                }
            }
        }
    }

}
