
package math() {
    /** A discrete signal with user-defined increments.
     */
    @python.intrinsic("observable.randomwalk._RandomWalk_Impl")
    @label = "%(name)s"
    def RandomWalk(/** initial value of the signal */ initialValue = 0.0,
                   /** increment function */ deltaDistr = math.random.normalvariate(0.0,1.0),
                   /** intervals between signal updates */ intervalDistr = math.random.expovariate(1.0),
                   name = "-random-") : IObservable[Float]
        
}
