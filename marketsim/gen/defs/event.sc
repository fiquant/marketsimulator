@category = "Event"
@method = "N/A"
package event
{
    /**
     *  Event that fires every *intervalFunc* moments of time
     */
    @python.intrinsic("event.Every_Impl")
    def Every(/** interval of time between two events */
              intervalFunc = math.random.expovariate(1.)) : IEvent

    /**
     * Event that once at *delay*
     */
    @python.intrinsic("event.After_Impl")
    def After(/** when the event should be fired */
              delay = constant(10.)) : IEvent


    type IScheduler

    /**
     * Scheduler that manages the future event set.
     * Must be a singleton
     */
    @python.intrinsic("scheduler.Scheduler_Impl")
    def createScheduler(currentTime = 0.) : IScheduler

    /**
     * Returns reference to the instance of the scheduler
     */
    @python.intrinsic("scheduler.currentScheduler_Impl")
    def Scheduler() : IScheduler

    type ISubscription

    @python.intrinsic("event.Subscription_Impl")
    def Subscription(event : Any, listener : Any) : ISubscription

    @python.intrinsic("event.Event_Impl")
    def Event() : IEvent

}
