package math
{
    @category = "Statistics"
    package Moving
    {
        /**
         *  Running minimum of a function
         */
        @python.intrinsic("observable.minmax.Min_Impl")
        @label = "Min_{n=%(timeframe)s}(%(source)s)"
        @method = "Moving_Min"
        def Min(/** observable data source */ source    = const(1.),
                /** sliding window size    */ timeframe = 100.) : IObservable[Float]

        /**
         *  Running maximum of a function
         */
        @python.intrinsic("observable.minmax.Max_Impl")
        @label = "Max_{n=%(timeframe)s}(%(source)s)"
        @method = "Moving_Max"
        def Max(/** observable data source */ source    = const(1.),
                /** sliding window size    */ timeframe = 100.) : IObservable[Float]
    }

    @category = "Statistics"
    package Cumulative
    {
        /**
         *  Cumulative minimum of a function with positive tolerance.
         *
         *  It fires updates only if *source* value becomes less than the old value minus *epsilon*
         */
        @python.intrinsic("observable.minmax_eps.MinEpsilon_Impl")
        @label = "Min_{\\epsilon}(%(source)s)"
        @method = "Cumulative_MinEpsilon"
        def MinEpsilon(/** observable data source */ source  = const(1.),
                       /** tolerance step         */ epsilon = constant(0.01)) : IObservable[Float]

        /**
         *  Cumulative maximum of a function with positive tolerance.
         *
         *  It fires updates only if *source* value becomes greater than the old value plus *epsilon*
         */
        @python.intrinsic("observable.minmax_eps.MaxEpsilon_Impl")
        @label = "Max_{\\epsilon}(%(source)s)"
        @method = "Cumulative_MaxEpsilon"
        def MaxEpsilon(/** observable data source */ source  = const(1.),
                       /** tolerance step         */ epsilon = constant(0.01)) : IObservable[Float]
    }

    package impl
    {
        def Minimum(x = .Moving()) = math.Moving.Min(x~>Source, x~>Timeframe)
        def Maximum(x = .Moving()) = math.Moving.Max(x~>Source, x~>Timeframe)

        @label = "Min_{\\epsilon}(%(x)s)"
        def MinEpsilon(x = .Cumulative(), epsilon = constant(0.01)) = math.Cumulative.MinEpsilon(x~>Source, epsilon)

        @label = "Max_{\\epsilon}(%(x)s)"
        def MaxEpsilon(x = .Cumulative(), epsilon = constant(0.01)) = math.Cumulative.MaxEpsilon(x~>Source, epsilon)

    }
}