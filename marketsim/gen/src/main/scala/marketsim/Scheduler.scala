package marketsim

import scala.collection.mutable

class Scheduler {

    type FutureEvent = (Time, Int, Callback)

    implicit object Ord extends Ordering[FutureEvent] {
        def compare(x: FutureEvent, y: FutureEvent) =
            x._1 compare y._1 match {
                case 0 => -(x._2 compare y._2)
                case z => -z
            }
    }

    private val future  = new mutable.PriorityQueue[FutureEvent]()
    private var next_id = 0
    private var t       = 0.0
    private var id      = -1

    def currentTime = t
    def eventId     = id

    def schedule(actionTime : Time, handler : Callback)
    {
        assert(actionTime >= t)
        future enqueue ((actionTime, next_id, handler))
        next_id += 1
    }

    def scheduleAfter(dt : Time, handler : Callback) = schedule(t + dt, handler)

    def async(handler : Callback) = schedule(t, handler)

    def step() =
        if (future.isEmpty)
            false
        else {
            val (event_time, event_id, handler) = future.dequeue()
            t  = event_time
            id = event_id
            handler()
            true
        }

    def workTill(limit : Time) =
    {
        var steps = 0
        while (t < limit && step())
            steps += 1
        t = limit
        steps
    }

    def advance(dt : Time) = workTill(t + dt)

    def process(intervals : () => Time, handler : Callback)
    {
        async(() => {
            handler()
            scheduleAfter(intervals(), () => process(intervals, handler))
        })
    }

}

