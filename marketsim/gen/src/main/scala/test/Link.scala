package test

import marketsim.Scheduler._

case object Link extends Test {

    def apply(trace : String => Unit)
    {
        marketsim.Scheduler.create { scheduler =>

            val link = new marketsim.orderbook.remote.Link(() => 20.0 - currentTime)

            0 to 5 foreach { i => schedule(i / 2.0, { link send {
                trace(s"t = $currentTime id = $i")
            }}) }

            scheduler workTill 100
        }
    }
}