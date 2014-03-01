package math
{
    @category = "Statistics"
    package
    {
        /**
         *  Running minimum of a function
         */
        @python.intrinsic("observable.minmax.Min_Impl")
        def Minimum(x = Moving()) : IObservable[Float]

        /**
         *  Running maximum of a function
         */
        @python.intrinsic("observable.minmax.Max_Impl")
        def Maximum(x = Moving()) : IObservable[Float]

        /**
         *  Cumulative minimum of a function with positive tolerance.
         *
         *  It fires updates only if *source* value becomes less than the old value minus *epsilon*
         */
        @python.intrinsic("observable.minmax_eps.MinEpsilon_Impl")
        @label = "Min_{\\epsilon}(%(x)s)"
        def MinEpsilon(x = Cumulative(), epsilon = constant(0.01)) : IObservable[Float]

        /**
         *  Cumulative maximum of a function with positive tolerance.
         *
         *  It fires updates only if *source* value becomes greater than the old value plus *epsilon*
         */
        @python.intrinsic("observable.minmax_eps.MaxEpsilon_Impl")
        @label = "Max_{\\epsilon}(%(x)s)"
        def MaxEpsilon(x = Cumulative(), epsilon = constant(0.01)) : IObservable[Float]
    }
}