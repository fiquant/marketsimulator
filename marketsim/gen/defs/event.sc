@category = "Event"
package event
{
    @python.intrinsic("event._Every_Impl")
    def Every(intervalFunc = math.random.expovariate(1.)) : IEvent

    @python.intrinsic("event._After_Impl")
    def After(delay = constant(10.)) : IEvent
}
