@category = "Event"

package event {
    /** Event that fires every *intervalFunc* moments of time
     */
    @python.intrinsic("event._Every_Impl")
    def Every(/** interval of time between two events */ intervalFunc = math.random.expovariate(1.0)) : IEvent // defined at defs\event.sc: 4.5
    
    /** Event that once at *delay*
     */
    @python.intrinsic("event._After_Impl")
    def After(/** when the event should be fired */ delay = constant(10.0)) : IEvent // defined at defs\event.sc: 11.5
}
