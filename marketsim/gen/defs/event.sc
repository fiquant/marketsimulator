@category = "Event"
package event
{
    @python.intrinsic("event._Every_Impl")
    def Every(intervalFunc = mathutils.rnd.expovariate(1.)) : IEvent

    @python.intrinsic("event._After_Impl")
    def After(delay = constant(10.)) : IEvent
}
