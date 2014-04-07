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
}
