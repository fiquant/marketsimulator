
package math {@category = "Statistics"
    
    package Moving {
        /** Running minimum of a function
         */
        @python.intrinsic("observable.minmax.Min_Impl")
        @label = "Min_{n=%(timeframe)s}(%(source)s)"
        def Min(/** observable data source */ source = constant(),
                /** sliding window size    */ timeframe = 100.0) : IObservable[Float]
        
        /** Running maximum of a function
         */
        @python.intrinsic("observable.minmax.Max_Impl")
        @label = "Max_{n=%(timeframe)s}(%(source)s)"
        def Max(/** observable data source */ source = constant(),
                /** sliding window size    */ timeframe = 100.0) : IObservable[Float]
    }
    @category = "Statistics"
    
    package Cumulative {
        /** Cumulative minimum of a function with positive tolerance.
         *
         *  It fires updates only if *source* value becomes less than the old value minus *epsilon*
         */
        @python.intrinsic("observable.minmax_eps.MinEpsilon_Impl")
        @label = "Min_{\\epsilon}(%(source)s)"
        def MinEpsilon(/** observable data source */ source = constant(),
                       /** tolerance step         */ epsilon = constant(0.01)) : IObservable[Float]
        
        /** Cumulative maximum of a function with positive tolerance.
         *
         *  It fires updates only if *source* value becomes greater than the old value plus *epsilon*
         */
        @python.intrinsic("observable.minmax_eps.MaxEpsilon_Impl")
        @label = "Max_{\\epsilon}(%(source)s)"
        def MaxEpsilon(/** observable data source */ source = constant(),
                       /** tolerance step         */ epsilon = constant(0.01)) : IObservable[Float]
    }
}
