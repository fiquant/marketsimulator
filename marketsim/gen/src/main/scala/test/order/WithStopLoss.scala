package test.order

import marketsim._
import marketsim.Scheduler._
import test._

case object WithStopLoss extends Test {

    def apply(trace_ : String => Unit)
    {
        def trace(s : String) = trace_(f"$currentTime%2.1f\t$s%s")

        marketsim.Scheduler.create { scheduler =>

            val local = new marketsim.orderbook.Local
            val link = new marketsim.orderbook.remote.TwoWayLink(() => 0.2, () => 0.3)
            val book = withLogging(trace)(new marketsim.orderbook.remote.Book(local, link))

            val A = new LoggedAccount(trace, book, "A")
            val B = new LoggedAccount(trace, book, "B")
            val C = new LoggedAccount(trace, book, "C")

            val sellOrders = LimitOrderFactory(() => 104 - currentTime.toInt, const(1))

            val stopOrders = marketsim.order.WithStopLoss.Factory(
                                    sellOrders, const(0.1f))

            val buyOrders = LimitOrderFactory(() => 95 + currentTime.toInt, const(-2))

            0 to 4 foreach { i => schedule(i,     A sendOrder sellOrders) }
            0 to 4 foreach { i => schedule(i,     C sendOrder stopOrders) }
            0 to 4 foreach { i => schedule(i + 5, B sendOrder buyOrders) }

            schedule(20, {
                A.ordersSent.getOrders foreach A.cancel
                B.ordersSent.getOrders foreach B.cancel
            })

            scheduler workTill 50
        }
    }
}
