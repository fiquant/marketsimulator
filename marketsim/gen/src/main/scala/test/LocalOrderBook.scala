package test

import marketsim._
import marketsim.Scheduler._

case object LocalOrderBook extends Test {

    def apply(trace : String => Unit)
    {
        def marketEvents(name : String) = OrderEvents[MarketOrder](trace, name)
        def limitEvents(name : String) = OrderEvents[LimitOrder](trace, name)

        marketsim.Scheduler.create { scheduler =>

            val book = new marketsim.orderbook.Local

            def sendLimit(price : Ticks, volume : Int) {
                val order = LimitOrder(price, volume, limitEvents("Limit[" + volume + "/" + price + "]"))
                trace("Sending" + order)
                trace("before = " + book)
                book handle order
                async {
                    trace("after = " + book)
                    trace("")
                }
            }

            0 to 4 foreach { i => schedule(i, sendLimit(100 + i, 1)) }
            0 to 4 foreach { i => schedule(i + 5, sendLimit(100 + i, -2)) }

            scheduler workTill 50
        }
    }
}