package test

import marketsim.orderbook.Entry
import marketsim._
import marketsim.orderbook.Entry
import marketsim.LimitOrder

case object OrderMatching extends Test {

    def apply(trace : String => Unit)
    {
        def marketEvents(name : String) = OrderEvents[MarketOrder](trace, name)
        def limitEvents(name : String) = OrderEvents[LimitOrder](trace, name)

        val sellOrder = Entry(LimitOrder(100, 10, limitEvents("Sell")))
        val buyOrder = Entry(LimitOrder(100, -10, limitEvents("Buy")))

        def matchOrder[T](order : Entry, other : Order[T])
        {
            other match {
                case x : LimitOrder if !(order canMatchWith x) =>
                case _ =>
                    val unmatchedOther = order matchWith (other, other.volumeAbsolute)
                    trace("Unmatched other = " + unmatchedOther)
                    trace("Unmatched sell = " + order.getVolumeUnmatched)
            }
        }

        matchOrder(sellOrder, MarketOrder(1, marketEvents("Market_Buy")))
        matchOrder(sellOrder, LimitOrder(120, -1, limitEvents("120_Buy")))
        matchOrder(sellOrder, LimitOrder(80, -1, limitEvents("80_Buy")))
        matchOrder(sellOrder, LimitOrder(100, -10, limitEvents("100_Buy")))

        matchOrder(buyOrder, MarketOrder(-1, marketEvents("Market_Sell")))
        matchOrder(buyOrder, LimitOrder(120, 1, limitEvents("120_Sell")))
        matchOrder(buyOrder, LimitOrder(80, 1, limitEvents("80_Sell")))
        matchOrder(buyOrder, LimitOrder(100, 10, limitEvents("100_Sell")))
    }
}
