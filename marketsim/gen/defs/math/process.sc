package math
{
    /**
     * A discrete signal with user-defined increments.
     */
    @python.intrinsic("observable.randomwalk._RandomWalk_Impl")
    @label = "%(name)s"
    def RandomWalk(/** initial value of the signal */      initialValue = 0.,
                   /** increment function */               deltaDistr   = random.normalvariate(0.,1.),
                   /** intervals between signal updates */ intervalDistr= random.expovariate(1.),
                   name = "-random-")
        : IObservable[Float]
}