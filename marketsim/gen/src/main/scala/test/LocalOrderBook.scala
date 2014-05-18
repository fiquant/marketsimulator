package test

import marketsim._
import marketsim.Scheduler._

case object LocalOrderBook extends Test {

    def apply(trace : String => Unit)
    {
        marketsim.Scheduler.create { scheduler =>

            val book = withLogging(trace)(new marketsim.orderbook.Local)
            val A = new LoggedAccount(trace, book, "A")
            val B = new LoggedAccount(trace, book, "B")

            val sellOrders = LimitOrderFactory(() => 100 + currentTime.toInt, () => 1)
            val buyOrders = LimitOrderFactory(() => 95 + currentTime.toInt, () => -2)

            0 to 4 foreach { i => schedule(i,     A sendOrder sellOrders) }
            0 to 4 foreach { i => schedule(i + 5, B sendOrder buyOrders) }

            schedule(10, {
                A.ordersSent.getOrders foreach A.cancel
                B.ordersSent.getOrders foreach B.cancel
            })

            scheduler workTill 50
        }
    }
}