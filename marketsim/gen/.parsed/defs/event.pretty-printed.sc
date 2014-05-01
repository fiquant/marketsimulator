@category = "Event"
@method = "N/A"

package event() {
    // defined at defs\event.sc: 5.5
    /** Event that fires every *intervalFunc* moments of time
     */
    @python.intrinsic("event.Every_Impl")
    def Every(/** interval of time between two events */ intervalFunc = math.random.expovariate(1.0)) : IEvent
    
    // defined at defs\event.sc: 12.5
    /** Event that once at *delay*
     */
    @python.intrinsic("event.After_Impl")
    def After(/** when the event should be fired */ delay = constant(10.0)) : IEvent
    
    type IScheduler
    
    // defined at defs\event.sc: 22.5
    /** Scheduler that manages the future event set.
     * Must be a singleton
     */
    @python.intrinsic("scheduler.Scheduler_Impl")
    def createScheduler(currentTime = 0.0) : IScheduler
    
    // defined at defs\event.sc: 29.5
    /** Returns reference to the instance of the scheduler
     */
    @python.intrinsic("scheduler.currentScheduler_Impl")
    def Scheduler() : IScheduler
    
    type ISubscription
    
    // defined at defs\event.sc: 37.5
    @python.intrinsic("event.Subscription_Impl")
    def Subscription(event : Any,
                     listener : Any) : ISubscription
    
    // defined at defs\event.sc: 40.5
    @python.intrinsic("event.Event_Impl")
    def Event() : IEvent
    
    // defined at defs\event.sc: 43.5
    @python.intrinsic("event.GreaterThan_Impl")
    def GreaterThan(bound : Float,
                    target : Any) : Any
    
    // defined at defs\event.sc: 46.5
    @python.intrinsic("event.LessThan_Impl")
    def LessThan(bound : Float,
                 target : Any) : Any
}
