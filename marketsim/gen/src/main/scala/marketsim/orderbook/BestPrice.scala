package marketsim.orderbook

import marketsim.{Observable, Ticks, OrderQueue}

case class BestPrice(queue : OrderQueue) extends Observable[Ticks]
{
    queue.BestPossiblyChanged += { pv => update(pv map { _._1 }) }
}
