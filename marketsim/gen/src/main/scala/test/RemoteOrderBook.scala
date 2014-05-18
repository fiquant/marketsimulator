package test

import marketsim._
import marketsim.Scheduler._

case object RemoteOrderBook extends Test {

    def apply(trace_ : String => Unit)
    {
        def trace(s : String) = trace_(f"[$eventId% 4d]  $currentTime%2.1f\t$s%s")

        marketsim.Scheduler.create { scheduler =>

            val local = new marketsim.orderbook.Local
            val link = new marketsim.orderbook.remote.TwoWayLink(() => 0.2, () => 0.3)
            val book = withLogging(trace)(new marketsim.orderbook.remote.Book(local, link))

            val account = new LoggedAccount(trace, book)

            val sellOrders = LimitOrderFactory(() => 100 + currentTime.toInt, () => 1)
            val buyOrders = LimitOrderFactory(() => 95 + currentTime.toInt, () => -2)

            0 to 4 foreach { i => schedule(i,     account sendOrder sellOrders) }
            0 to 4 foreach { i => schedule(i + 5, account sendOrder buyOrders) }

            schedule(10, {
                account.ordersSent.getOrders foreach account.cancel
            })

            scheduler workTill 50
        }
    }
}
