package marketsim

package object orderbook {

    import marketsim.{OptObservable, Ticks, OrderQueue}

    case class BestPriceVolume_(queue : OrderQueue) extends OptObservable[PriceVolume]
    {
        queue.BestPossiblyChanged += update
    }

    object BestPriceVolume
    {
        private val cache = collection.mutable.HashMap.empty[OrderQueue, BestPriceVolume_]

        def apply(queue : OrderQueue) = cache getOrElseUpdate(queue, new BestPriceVolume_(queue))
    }

    case class BestPrice_(queue : OrderQueue) extends OptObservable[Ticks]
    {
        BestPriceVolume(queue) += { pv => update(pv map { _._1 }) }
    }

    object BestPrice
    {
        private val cache = collection.mutable.HashMap.empty[OrderQueue, BestPrice_]

        def apply(queue : OrderQueue) = cache getOrElseUpdate(queue, new BestPrice_(queue))
    }

    case class BestVolume_(queue : OrderQueue) extends OptObservable[Int]
    {
        BestPriceVolume(queue) += { pv => update(pv map { _._2 }) }
    }

    object BestVolume
    {
        private val cache = collection.mutable.HashMap.empty[OrderQueue, BestVolume_]

        def apply(queue : OrderQueue) = cache getOrElseUpdate(queue, new BestVolume_(queue))
    }

    case class LastTradePriceVolume_(queue : OrderQueue) extends OptObservable[PriceVolume]
    {
        queue.TradeDone += { pv => update(Some(pv)) }
    }

    object LastTradePriceVolume
    {
        private val cache = collection.mutable.HashMap.empty[OrderQueue, LastTradePriceVolume_]

        def apply(queue : OrderQueue) = cache getOrElseUpdate(queue, new LastTradePriceVolume_(queue))
    }

    case class LastTradePrice_(queue : OrderQueue) extends OptObservable[Ticks]
    {
        LastTradePriceVolume(queue) += { pv => update(pv map { _._1 }) }
    }

    object LastTradePrice
    {
        private val cache = collection.mutable.HashMap.empty[OrderQueue, LastTradePrice_]

        def apply(queue : OrderQueue) = cache getOrElseUpdate(queue, new LastTradePrice_(queue))
    }

    //case class IfDefined[T](source : ) extends Observable[T]

    case class SafeSidePrice(queue : OrderQueue) extends OptObservable[Ticks]
    {

    }
}

