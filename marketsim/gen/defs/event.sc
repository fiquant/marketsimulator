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

    // we should have also defined Suscription
    // but currently type system doesn't allow generic functions
}
