package marketsim

package object orderbook {

    import marketsim.{Observable, Ticks, OrderQueue}

    case class BestPriceVolume_(queue : OrderQueue) extends Observable[PriceVolume]
    {
        queue.BestPossiblyChanged += update
    }

    object BestPriceVolume
    {
        private val cache = collection.mutable.HashMap.empty[OrderQueue, BestPriceVolume_]

        def apply(queue : OrderQueue) = cache getOrElseUpdate(queue, new BestPriceVolume_(queue))
    }

    case class BestPrice_(queue : OrderQueue) extends Observable[Ticks]
    {
        BestPriceVolume(queue) += { pv => update(pv map { _._1 }) }
    }

    object BestPrice
    {
        private val cache = collection.mutable.HashMap.empty[OrderQueue, BestPrice_]

        def apply(queue : OrderQueue) = cache getOrElseUpdate(queue, new BestPrice_(queue))
    }

    case class BestVolume_(queue : OrderQueue) extends Observable[Int]
    {
        BestPriceVolume(queue) += { pv => update(pv map { _._2 }) }
    }

    object BestVolume
    {
        private val cache = collection.mutable.HashMap.empty[OrderQueue, BestVolume_]

        def apply(queue : OrderQueue) = cache getOrElseUpdate(queue, new BestVolume_(queue))
    }
}
