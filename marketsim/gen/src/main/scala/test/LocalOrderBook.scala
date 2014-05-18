package test

import marketsim._
import marketsim.Scheduler._

case object LocalOrderBook extends Test {

    def apply(trace : String => Unit)
    {
        marketsim.Scheduler.create { scheduler =>

            val book = withLogging(trace)(new marketsim.orderbook.Local)
            val account = new LoggedAccount(trace, book)

            val sellOrders = LimitOrderFactory(() => 100 + currentTime.toInt, () => 1)
            val buyOrders = LimitOrderFactory(() => 95 + currentTime.toInt, () => -2)

            0 to 4 foreach { i => schedule(i, account sendOrder sellOrders) }
            0 to 4 foreach { i => schedule(i + 5, account sendOrder buyOrders) }

            schedule(10, {
                account.ordersSent.getOrders foreach account.cancel
            })

            scheduler workTill 50
        }
    }
}