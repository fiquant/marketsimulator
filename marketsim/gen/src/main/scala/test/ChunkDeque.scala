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

        def insert(p : Int) =
        {
            trace("Inserting " + p)
            val order = LimitOrder(p, 1, LimitOrderEvents("Limit_Sell_" + p))
            deque insert SellEntry(order)
            trace("Best = " + deque.top.order.toString)
            order
        }

        def cancel(order : LimitOrder)
        {
            trace(s"Cancel $order -> " + (deque cancel order))
        }

        def pop()
        {
            trace("popping")
            deque.pop()
            if (deque.isEmpty)
                trace("Empty = true")
            else
                trace("Best = " + deque.top.order.toString)
        }

        insert(32)
        insert(31)
        insert(52)
        insert(12)
        insert(52)

        cancel(insert(9))
        cancel(insert(32))
        cancel(insert(40))
        cancel(insert(77))

        pop()
        pop()
        pop()
        pop()
        pop()
    }

}
