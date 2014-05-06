package test

import marketsim.orderbook.Entry
import marketsim._
import marketsim.orderbook.Entry
import marketsim.LimitOrder

object OrderMatching {

    var result = List.empty[String]

    def trace(p : Any)
    {
        result = p.toString :: result
    }

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

        override def toString = "X"
    }

    def main(args : Array[String]) {

        val sellOrder = Entry(LimitOrder(100, 10, LimitOrderEvents("Sell")))

        def sellOrderMatch[T](other : Order[T], volume : Volume)
        {
            other match {
                case x : LimitOrder if !(sellOrder canMatchWith x) =>
                case _ =>
                    val unmatchedOther = sellOrder matchWith (other, volume)
                    trace("Unmatched other = " + unmatchedOther)
                    trace("Unmatched sell = " + sellOrder.getVolumeUnmatched)
            }
        }

        sellOrderMatch(MarketOrder(1, MarketOrderEvents("Market_Buy")), 1)
        sellOrderMatch(LimitOrder(120, -1, LimitOrderEvents("120_Buy")), 1)
        sellOrderMatch(LimitOrder(80, -1, LimitOrderEvents("80_Buy")), 1)
        sellOrderMatch(LimitOrder(100, -10, LimitOrderEvents("100_Buy")), 10)

        scala.tools.nsc.io.File("test_result/order_matching.result").writeAll(result.reverse mkString "\n")
    }

}
