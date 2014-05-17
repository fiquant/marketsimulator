package test

import marketsim.orderbook.SellEntry
import marketsim._
import marketsim.LimitOrder

case object ChunkDeque extends Test {

    def apply(trace : String => Unit)
    {
        def limitEvents(name : String) = OrderEvents(trace, name)

        val deque = new marketsim.orderbook.ChunkDeque[SellEntry]()

        def epilogue()
        {
            trace("cumPrice(3) = " + deque.cumulativePrice(3))
            trace(s"priceForVolumes([1,3,5]) = " + deque.getPricesForVolumes(1 :: 3 :: 5 :: Nil).mkString("[",",","]"))
            trace(deque + "\n")
        }

        def insert(p : Int) =
        {
            trace("Inserting " + p)
            val order = LimitOrder(p, 1)
            deque insert SellEntry(order, limitEvents("Limit_Sell_" + p))
            trace("Best = " + deque.top.order.toString)
            epilogue()
            order
        }

        def cancel(order : LimitOrder)
        {
            trace(s"Cancel $order -> " + (deque cancel order).get.getVolumeUnmatched)
            epilogue()
        }

        def pop()
        {
            trace("popping")
            deque.pop()
            if (deque.isEmpty)
                trace("Empty = true")
            else
                trace("Best = " + deque.top.order.toString)
            epilogue()
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
