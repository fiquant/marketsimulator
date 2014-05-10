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
        future += ((actionTime, next_id, handler))
        next_id += 1
    }

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
}

object Scheduler
{
    private var instance = Option.empty[Scheduler]

    def create(f : Scheduler => Unit)
    {
        assert(instance.isEmpty)
        instance = Some(new Scheduler)
        f(instance.get)
        instance = None
    }

    def currentTime = instance.get.currentTime
    def eventId     = instance.get.eventId

    def schedule(actionTime : Time, handler : Callback) = instance.get.schedule(actionTime, handler)

    def scheduleAfter(dt : Time, handler : Callback) = schedule(currentTime + dt, handler)

    def async(handler : Callback) = schedule(currentTime, handler)

    def step() = instance.get.step()

    def workTill(limit : Time) = instance.get.workTill(limit)

    def advance(dt : Time) = workTill(currentTime + dt)

    def process(intervals : () => Time, handler : Callback)
    {
        async(() => {
            handler()
            scheduleAfter(intervals(), () => process(intervals, handler))
        })
    }

}
