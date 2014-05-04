package test

object Scheduler {

    def main(args : Array[String]) {

        import marketsim.Scheduler

        val scheduler = new Scheduler()
        var result = List.empty[(Double, Int)]

        def callback()
        {
            result = (scheduler.currentTime, scheduler.eventId) :: result
        }

        0 to 10 foreach { i => scheduler.schedule(i, callback) }

        scheduler.process(() => 2.0, callback)
        scheduler.process(() => 3.0, callback)
        scheduler.process(() => 6.0, callback)

        scheduler.workTill(60.0)

        scala.tools.nsc.io.File("test_result/scheduler.result").writeAll(result.reverse mkString "\n")
    }

}
