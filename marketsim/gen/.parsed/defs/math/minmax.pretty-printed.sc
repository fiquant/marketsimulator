
package math() {@category = "Statistics"
    
    package Moving() {
        // defined at defs\math\minmax.sc: 6.9
        /** Running minimum of a function
         */
        @python.intrinsic("observable.minmax.Min_Impl")
        @label = "Min_{n=%(timeframe)s}(%(source)s)"
        @method = "Moving_Min"
        def Min(/** observable data source */ source = const(1.0),
                /** sliding window size    */ timeframe = 100.0) : IObservable[Float]
        
        // defined at defs\math\minmax.sc: 15.9
        /** Running maximum of a function
         */
        @python.intrinsic("observable.minmax.Max_Impl")
        @label = "Max_{n=%(timeframe)s}(%(source)s)"
        @method = "Moving_Max"
        def Max(/** observable data source */ source = const(1.0),
                /** sliding window size    */ timeframe = 100.0) : IObservable[Float]
    }
    @category = "Statistics"
    
    package Cumulative() {
        // defined at defs\math\minmax.sc: 28.9
        /** Cumulative minimum of a function with positive tolerance.
         *
         *  It fires updates only if *source* value becomes less than the old value minus *epsilon*
         */
        @python.intrinsic("observable.minmax_eps.MinEpsilon_Impl")
        @label = "Min_{\\epsilon}(%(source)s)"
        @method = "Cumulative_MinEpsilon"
        def MinEpsilon(/** observable data source */ source = const(1.0),
                       /** tolerance step         */ epsilon = constant(0.01)) : IObservable[Float]
        
        // defined at defs\math\minmax.sc: 39.9
        /** Cumulative maximum of a function with positive tolerance.
         *
         *  It fires updates only if *source* value becomes greater than the old value plus *epsilon*
         */
        @python.intrinsic("observable.minmax_eps.MaxEpsilon_Impl")
        @label = "Max_{\\epsilon}(%(source)s)"
        @method = "Cumulative_MaxEpsilon"
        def MaxEpsilon(/** observable data source */ source = const(1.0),
                       /** tolerance step         */ epsilon = constant(0.01)) : IObservable[Float]
    }
    
    package impl() {
        // defined at defs\math\minmax.sc: 53.9
        def Minimum(x = .Moving()) = math.Moving.Min(x~>Source,x~>Timeframe)
        
        // defined at defs\math\minmax.sc: 54.9
        def Maximum(x = .Moving()) = math.Moving.Max(x~>Source,x~>Timeframe)
        
        // defined at defs\math\minmax.sc: 56.9
        @label = "Min_{\\epsilon}(%(x)s)"
        def MinEpsilon(x = .Cumulative(),
                       epsilon = constant(0.01)) = math.Cumulative.MinEpsilon(x~>Source,epsilon)
        
        // defined at defs\math\minmax.sc: 59.9
        @label = "Max_{\\epsilon}(%(x)s)"
        def MaxEpsilon(x = .Cumulative(),
                       epsilon = constant(0.01)) = math.Cumulative.MaxEpsilon(x~>Source,epsilon)
    }
}
