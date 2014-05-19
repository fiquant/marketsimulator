package marketsim.orderbook

import marketsim.{Observable, Ticks, OrderQueue}

case class BestPrice(queue : OrderQueue) extends Observable[Ticks]
{
    queue.BestPossiblyChanged += update
}
