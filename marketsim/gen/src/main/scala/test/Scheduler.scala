package test

case object Scheduler extends Test {

    def apply(trace : String => Unit) {

        import marketsim.Scheduler.{process, schedule}

        marketsim.Scheduler.create({ scheduler =>
            def callback()
            {
                trace((scheduler.currentTime, scheduler.eventId).toString())
            }

            0 to 10 foreach { i => schedule(i, callback) }

            process(() => 2.0, callback)
            process(() => 3.0, callback)
            process(() => 6.0, callback)

            scheduler.workTill(60.0)

        })

    }

}
