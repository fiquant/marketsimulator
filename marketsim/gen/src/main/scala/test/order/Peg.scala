package test.order

import marketsim._
import marketsim.Scheduler._
import test._

case object Peg extends Test {

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

            val sellOrders = LimitOrderFactory(() => 104 - currentTime.toInt, const(10))
            val sellPeg = marketsim.order.Peg.Factory(LimitOrderFactory(const(33), const(55)))
            val buyOrders = LimitOrderFactory(() => 95 + currentTime.toInt, const(-10))

            schedule(0, C sendOrder sellPeg)
            0 to 4 foreach { i => schedule(i,     A sendOrder sellOrders) }
            0 to 4 foreach { i => schedule(5 + i, B sendOrder buyOrders) }

            schedule(20, {
                A.ordersSent.getOrders foreach A.cancel
                B.ordersSent.getOrders foreach B.cancel
                C.ordersSent.getOrders foreach C.cancel
            })

            scheduler workTill 50
        }
    }
}
