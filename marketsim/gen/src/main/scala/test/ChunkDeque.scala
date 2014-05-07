package test

import marketsim.orderbook.SellEntry
import marketsim._
import marketsim.LimitOrder

case object ChunkDeque extends Test {

    def apply(trace : String => Unit)
    {
        case class LimitOrderEvents(name : String) extends LimitOrderListener
        {
            def OnTraded(order : LimitOrder, price : Ticks, volume : Volume)
            {
                trace(s"$order traded at $price with $volume")
            }

            def OnMatched(order : LimitOrder)
            {
                trace(s"$order matched completely")
            }

            def OnCancelled(order : LimitOrder)
            {
                trace(s"$order cancelled")
            }

            override def toString = name
        }

        val deque = new marketsim.orderbook.ChunkDeque[SellEntry]()

        deque insert SellEntry(LimitOrder(12, 1, LimitOrderEvents("Limit_Sell")))

        trace(deque.top.order.toString)
    }

}
