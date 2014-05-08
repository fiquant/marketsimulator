package marketsim.orderbook

import marketsim.{Sell, LimitOrder}

class ChunkDeque[T <: Entry](chunkSize : Int = 10) {

    class Chunk
    {
        class Queue(initial : Entry)
        {
            private var impl = scala.collection.immutable.Queue[Entry](initial)
            private var volume = initial.getVolumeUnmatched

            def getVolume = volume

            def push(x : Entry)
            {
                impl = impl enqueue x
                volume += x.getVolumeUnmatched
            }

            def pop() =
            {
                volume -= impl.front.getVolumeUnmatched
                impl = impl.dequeue._2
                isEmpty
            }

            def isEmpty = impl.isEmpty

            def top = impl.front

            def remove(x : LimitOrder)  =
            {
                val (found, rest) = impl partition { _.order eq x }
                assert(found.length < 2)
                impl = rest
                if (found.length == 1)
                    volume -= found.front.getVolumeUnmatched
                found.nonEmpty
            }

            override def toString =  volume + "/" + impl.front.order.price
        }

        private val impl = new Array[Queue](chunkSize)

        override def toString = impl filter { _ != null } mkString " "

        def get(idx : Int) = impl(idx)

        def push(idx : Int, x : Entry) =
            impl(idx) match {
                case null => impl(idx) = new Queue(x)
                case queue => queue push x
            }

        /**
         *  Believes that the best element is in 'idx' position and pops it away
         * @param idx index of element to pop away
         * @return delta between indices of the new best element and the old.
         *         this delta is negative if current chunk becomes empty
         */
        def pop(idx : Int) = {
            if (impl(idx).pop()) {
                impl(idx) = null
                (impl indexWhere ({ _ != null}, idx)) - idx
            } else
                0
        }

        def isEmpty = impl forall { _ == null }

        /**
         * Removes entry with 'order' that should reside at position 'idx'
         * @return true iff the element is actually removed
         */
        def remove(idx : Int, order : LimitOrder) =
        {
            impl(idx) match {
                case null => false
                case queue =>
                    if (queue remove order)
                    {
                        if (queue.isEmpty)
                            impl(idx) = null
                        true
                    } else
                        false
            }
        }

        def idxOfBest = impl indexWhere { _ != null }
    }

    private var chunks = Array.empty[Chunk]

    // index of the first allocated chunk
    private var base   = -1

    // index in chunk of the best order queue
    private var topIdx = Int.MaxValue

    override def toString = chunks filter { _ != null } mkString " "

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
            chunks(chunkIdx - base) = new Chunk

        val myChunk = chunks(chunkIdx - base)

        val relIdx =   key - chunkIdx * chunkSize

        myChunk push (relIdx, x)

        if (key < topIdx)
            topIdx = key
    }

    def top = {
        assert(chunks.nonEmpty)
        chunks(0).get(topIdx - base*chunkSize).top
    }

    def isEmpty = chunks.isEmpty

    def pop() {
        assert(!isEmpty)
        val relIdx = topIdx - base*chunkSize
        val myChunk = chunks(0)

        myChunk pop relIdx match
        {
            case delta if delta >= 0 => topIdx += delta
            case _ =>
                chunks(0) = null
                val firstNonNull = chunks.indexWhere({ _ != null })
                if (firstNonNull == -1) {
                    chunks = Array.empty[Chunk]
                } else {
                    chunks = chunks.slice(firstNonNull, chunks.length )
                    base += firstNonNull
                    topIdx = chunks(0).idxOfBest + base*chunkSize
                }

        }
    }

    def cancel(order : LimitOrder) = {
        if (isEmpty)
            false
        else {
            if (order eq top.order) {
                pop()
                true
            } else {
                // unfortunately we cannot access static members of T
                val key = if (order.side == Sell) order.price else -order.price
                val chunkIdx = if (key > 0) key / chunkSize else key / chunkSize - 1
                if (base <= chunkIdx && chunkIdx < base + chunks.length)
                {
                    chunks(chunkIdx - base) match {
                        case null => false
                        case myChunk =>
                            val relIdx = key - chunkIdx * chunkSize
                            if (myChunk remove (relIdx, order))
                            {
                                if (myChunk.isEmpty) {
                                    chunks(chunkIdx - base) = null
                                    if (chunkIdx == base + chunks.length - 1) {
                                        val lastIdx = chunks lastIndexWhere { _ != null }
                                        if (lastIdx == -1)
                                            chunks = Array.empty[Chunk]
                                        else
                                            chunks = chunks slice (0, lastIdx + 1)
                                    }
                                }
                                true
                            } else
                                false
                    }
                }
                else
                    false
            }
        }
    }

}
