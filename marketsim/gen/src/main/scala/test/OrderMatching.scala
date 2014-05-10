package test

import marketsim.orderbook.Entry
import marketsim._
import marketsim.orderbook.Entry
import marketsim.LimitOrder

case object OrderMatching extends Test {

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

        case class MarketOrderEvents(name : String) extends MarketOrderListener
        {
            def OnTraded(order : MarketOrder, price : Ticks, volume : Volume)
            {
                trace(s"$order traded at $price with $volume")
            }

            def OnMatched(order : MarketOrder)
            {
                trace(s"$order matched completely")
            }

            def OnCancelled(order : MarketOrder)
            {
                trace(s"$order cancelled")
            }

            override def toString = "X"
        }

        val sellOrder = Entry(LimitOrder(100, 10, LimitOrderEvents("Sell")))
        val buyOrder = Entry(LimitOrder(100, -10, LimitOrderEvents("Buy")))

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

        matchOrder(sellOrder, MarketOrder(1, MarketOrderEvents("Market_Buy")))
        matchOrder(sellOrder, LimitOrder(120, -1, LimitOrderEvents("120_Buy")))
        matchOrder(sellOrder, LimitOrder(80, -1, LimitOrderEvents("80_Buy")))
        matchOrder(sellOrder, LimitOrder(100, -10, LimitOrderEvents("100_Buy")))

        matchOrder(buyOrder, MarketOrder(-1, MarketOrderEvents("Market_Sell")))
        matchOrder(buyOrder, LimitOrder(120, 1, LimitOrderEvents("120_Sell")))
        matchOrder(buyOrder, LimitOrder(80, 1, LimitOrderEvents("80_Sell")))
        matchOrder(buyOrder, LimitOrder(100, 10, LimitOrderEvents("100_Sell")))
    }
}
