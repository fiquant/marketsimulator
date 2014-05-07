package test

case object Scheduler extends Test {

    def apply(trace : String => Unit) {

        import marketsim.Scheduler

        val scheduler = new Scheduler()

        def callback()
        {
            trace((scheduler.currentTime, scheduler.eventId).toString())
        }

        0 to 10 foreach { i => scheduler.schedule(i, callback) }

        scheduler.process(() => 2.0, callback)
        scheduler.process(() => 3.0, callback)
        scheduler.process(() => 6.0, callback)

        scheduler.workTill(60.0)
    }

}
