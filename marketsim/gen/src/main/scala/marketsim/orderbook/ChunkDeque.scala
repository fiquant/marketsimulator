package marketsim.orderbook

import marketsim.{Ticks, Sell, LimitOrder}

class ChunkDeque[T <: Entry](chunkSize : Int = 10) {

    deque =>

    private class Chunk
    {
        chunk =>

        class Queue(initial : T)
        {
            private var impl = scala.collection.immutable.Queue[T](initial)
            private var volume = 0
            changeVolume(initial.getVolumeUnmatched)

            private def changeVolume(delta : Int, price : Ticks)
            {
                volume += delta
                chunk.volume += delta
                chunk.price += delta * price
            }

            private[ChunkDeque] def changeVolume(delta : Int) { changeVolume(delta, price) }

            def price = impl.front.order.price

            def getVolume = volume

            def push(x : T)
            {
                impl = impl enqueue x
                changeVolume(x.getVolumeUnmatched)
            }

            def pop() =
            {
                changeVolume(-impl.front.getVolumeUnmatched)
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
                if (found.length == 1) {
                    changeVolume(-found.front.getVolumeUnmatched, x.price)
                    Some(found.front)
                }
                else None
            }

            def getPricesForVolumes(volumes : List[Int],
                                    cont : List[Int] => List[Ticks]) =
            {
                def inner(volumeUsed : Int, volumes : List[Int]) : List[Ticks] =
                {
                    if (volumes.isEmpty) Nil
                    else {
                        if (volumes.head <= volume - volumeUsed) {
                            price :: inner(volumes.head + volumeUsed, volumes.tail)
                        } else {
                            cont((volumes.head - volume + volumeUsed) :: volumes.tail)
                        }
                    }
                }
                inner(0, volumes)
            }

            override def toString =  volume + "/" + impl.front.order.price
        }

        private val impl = new Array[Queue](chunkSize)
        private var volume = 0
        private var price = 0

        def getVolume = volume
        def getPrice = price

        override def toString = impl filter { _ != null } mkString " "

        def cumulativePrice(volume : Int) =
        {
            var v = 0
            var p = 0

            (impl.toStream
                    filter    { _ != null }
                    takeWhile { _ => v < volume }
                    foreach   { queue =>
                                    val d = queue.getVolume min (volume - v)
                                    v += d
                                    p += d * queue.price
                              })

            p
        }

        /**
         * Returns prices corresponding to given volume levels.
         * If there is no corresponding volume level returns -1
         * @param volumes - volumes requested. should be in range [baseVolume, baseVolume + volume)
         */
        def getPricesForVolumes(volumes : List[Int],
                                cont : List[Int] => List[Ticks])  =
        {
            def inner(rest : Stream[Queue], volumes : List[Int]) : List[Ticks] =
            {
                rest match {
                    case Stream.Empty => cont(volumes)
                    case q #:: qs =>
                        if (volumes.isEmpty) Nil
                        else {
                            if (volumes.head <= q.getVolume) {
                                q.getPricesForVolumes(volumes, { unfilled => inner(qs, unfilled) })
                            } else {
                                inner(qs, (volumes.head - q.getVolume) :: volumes.tail)
                            }
                        }
                }
            }

            inner(impl.toStream filter { _ != null}, volumes)
        }

        def get(idx : Int) = impl(idx)

        def push(idx : Int, x : T) =
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

        def isEmpty = volume == 0

        /**
         * Removes entry with 'order' that should reside at position 'idx'
         * @return unmatched volume of the removed order
         */
        def remove(idx : Int, order : LimitOrder) =
        {
            impl(idx) match {
                case null => None
                case queue =>
                    val ret = queue remove order

                    if (!ret.isEmpty)
                    {
                        if (queue.isEmpty)
                            impl(idx) = null
                    }

                    ret
            }
        }

        def idxOfBest = impl indexWhere { _ != null }
    }

    private var chunks = Array.empty[Chunk]

    // index of the first allocated chunk
    private var base   = -1

    // index in chunk of the best order queue
    private var topIdx = Int.MaxValue

    override def toString = chunks filter { _ != null } mkString ("[", " ", "]")

    private def toPosition(x : Int) =
        if (x < 0) (x / chunkSize, x % chunkSize + chunkSize - 1)
        else       (x / chunkSize, x % chunkSize)

    private def fromPosition(chunkIdx : Int, relIdx : Int) =
        if (chunkIdx < 0) chunkIdx * chunkSize + relIdx - chunkSize + 1
        else              chunkIdx * chunkSize + relIdx

    def insert(x : T)
    {
        val key = x.signedTicks
        val (chunkIdx, relIdx) = toPosition(key)

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

        myChunk push (relIdx, x)

        if (key < topIdx)
            topIdx = key
    }

    def top = {
        assert(chunks.nonEmpty)
        chunks(0).get(toPosition(topIdx)._2).top
    }

    def takeVolumeFromTop(deltaVolume : Int) =
        chunks(0) get toPosition(topIdx)._2 changeVolume -deltaVolume

    def getTopPriceVolume = {
        val queue = chunks(0) get toPosition(topIdx)._2
        (queue.price, queue.getVolume)
    }

    def isEmpty = chunks.isEmpty

    def cumulativePrice(volume : Int) =
    {
        var v = 0
        var p = 0

        (chunks.toStream
                filter      { _ != null }
                takeWhile   { _ => v < volume }
                foreach     { chunk =>
                                if (volume - v < chunk.getVolume)
                                {
                                    p += chunk.cumulativePrice(volume - v)
                                    v  = volume
                                } else {
                                    v += chunk.getVolume
                                    p += chunk.getPrice
                                }
        })

        if (v < volume) -1 else p
    }

    def getPricesForVolumes(volumes : List[Int]) : List[Ticks] =
    {
        def inner(rest : Stream[Chunk], volumes : List[Int]) : List[Ticks] =
        {
            rest match {
                case Stream.Empty => List.fill(volumes.length){ -1 }
                case ch #:: chs =>
                    if (volumes.isEmpty) Nil
                    else {
                        if (volumes.head <= ch.getVolume) {
                            ch.getPricesForVolumes(volumes, { unfilled => inner(chs, unfilled) })
                        } else {
                            inner(chs, (volumes.head - ch.getVolume) :: volumes.tail)
                        }
                    }
            }
        }
        def differences(l:List[Int]) : List[Int] = l match {
          case a :: (rest @ b :: _) => (b - a) :: differences(rest)
          case _ => Nil
        }

        inner(chunks.toStream filter { _ != null }, volumes.head :: differences(volumes))
    }

    def pop() {
        assert(!isEmpty)
        val relIdx = toPosition(topIdx)._2
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
            None
        else {
            if (order eq top.order) {
                val ret = top
                pop()
                Some(ret)
            } else {
                // unfortunately we cannot access static members of T
                val key = if (order.side == Sell) order.price else -order.price
                val (chunkIdx, relIdx) = toPosition(key)
                if (base <= chunkIdx && chunkIdx < base + chunks.length)
                {
                    chunks(chunkIdx - base) match {
                        case null => None
                        case myChunk =>
                            val ret = myChunk remove (relIdx, order)
                            if (!ret.isEmpty)
                            {
                                if (myChunk.isEmpty) {
                                    chunks(chunkIdx - base) = null
                                    if (chunkIdx == base + chunks.length - 1) {
                                        val lastIdx = chunks lastIndexWhere { _ != null }
                                        chunks = if (lastIdx == -1) Array.empty[Chunk] else chunks slice (0, lastIdx + 1)
                                    }
                                }
                            }
                            ret
                    }
                }
                else
                    None
            }
        }
    }

}
