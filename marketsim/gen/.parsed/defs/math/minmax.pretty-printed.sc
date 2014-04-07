
package math() {@category = "Statistics"
    
    package () {
        // defined at defs/math/minmax.sc: 6.9
        /** Running minimum of a function
         */
        @python.intrinsic("observable.minmax.Min_Impl")
        def Minimum(x = Moving()) : IObservable[Float]
        
        // defined at defs/math/minmax.sc: 12.9
        /** Running maximum of a function
         */
        @python.intrinsic("observable.minmax.Max_Impl")
        def Maximum(x = Moving()) : IObservable[Float]
        
        // defined at defs/math/minmax.sc: 18.9
        /** Cumulative minimum of a function with positive tolerance.
         *
         *  It fires updates only if *source* value becomes less than the old value minus *epsilon*
         */
        @python.intrinsic("observable.minmax_eps.MinEpsilon_Impl")
        @label = "Min_{\\epsilon}(%(x)s)"
        def MinEpsilon(x = Cumulative(),
                       epsilon = constant(0.01)) : IObservable[Float]
        
        // defined at defs/math/minmax.sc: 27.9
        /** Cumulative maximum of a function with positive tolerance.
         *
         *  It fires updates only if *source* value becomes greater than the old value plus *epsilon*
         */
        @python.intrinsic("observable.minmax_eps.MaxEpsilon_Impl")
        @label = "Max_{\\epsilon}(%(x)s)"
        def MaxEpsilon(x = Cumulative(),
                       epsilon = constant(0.01)) : IObservable[Float]
    }
}
