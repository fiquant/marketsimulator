
package math() {@category = "Statistics"
    
    package Moving() {
        @python.intrinsic("observable.minmax.Min_Impl")
        @label = "Min_{n=%(timeframe)s}(%(source)s)"
        def Min(source = constant(),
                timeframe = 100.0) : IObservable[Float]
            
        
        @python.intrinsic("observable.minmax.Max_Impl")
        @label = "Max_{n=%(timeframe)s}(%(source)s)"
        def Max(source = constant(),
                timeframe = 100.0) : IObservable[Float]
            
    }
    @category = "Statistics"
    
    package Cumulative() {
        @python.intrinsic("observable.minmax_eps.MinEpsilon_Impl")
        @label = "Min_{\\epsilon}(%(source)s)"
        def MinEpsilon(source = constant(),
                       epsilon = constant(0.01)) : IObservable[Float]
            
        
        @python.intrinsic("observable.minmax_eps.MaxEpsilon_Impl")
        @label = "Max_{\\epsilon}(%(source)s)"
        def MaxEpsilon(source = constant(),
                       epsilon = constant(0.01)) : IObservable[Float]
            
    }
}
