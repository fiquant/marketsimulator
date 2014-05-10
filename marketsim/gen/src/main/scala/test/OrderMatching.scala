package test

import marketsim.orderbook.{SellEntry, Entry}
import marketsim._
import marketsim.LimitOrder

case object OrderMatching extends Test {

    def apply(trace : String => Unit)
    {
        def marketEvents(name : String) = OrderEvents[MarketOrder](trace, name)
        def limitEvents(name : String) = OrderEvents[LimitOrder](trace, name)

        marketsim.Scheduler.create({ scheduler =>

            val asks = new marketsim.orderbook.Queue[SellEntry]

            import marketsim.Scheduler.{async, schedule}

            def sendLimit(price : Ticks, volume : Int) {
                val order = LimitOrder(price, -volume, limitEvents(price + "_Buy"))
                trace("Sending" + order)
                trace("before = " + asks)
                val res = asks matchWith order
                async {
                    trace("Unfilled = " + res)
                    trace("after = " + asks)
                    trace("")
                }
            }

            def sendMarket(volume : Int) {
                val order = MarketOrder(-volume, marketEvents("Market_Buy"))
                trace("Sending" + order)
                trace("before = " + asks)
                val res = asks matchWith order
                async {
                    trace("Unfilled = " + res)
                    trace("after = " + asks)
                    trace("")
                }
            }

            schedule(0, asks insert new SellEntry(LimitOrder(100, 10, limitEvents("Sell_1_100"))))

            schedule(1, sendMarket(1))
            schedule(2, sendLimit(120, 1))
            schedule(3, sendLimit(80, 1))
            schedule(4, sendLimit(100, 10))

            schedule(5, asks insert new SellEntry(LimitOrder(100, 10, limitEvents("Sell_2_100"))))
            schedule(6, asks insert new SellEntry(LimitOrder(100, 10, limitEvents("Sell_3_100"))))
            schedule(7, asks insert new SellEntry(LimitOrder(103, 10, limitEvents("Sell_1_103"))))

            schedule(8, sendLimit(100, 15))
            schedule(9, sendLimit(105, 20))

            scheduler workTill 10
        })
    }
}
