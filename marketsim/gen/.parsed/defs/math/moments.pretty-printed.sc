
package math() {@category = "Statistics"
    
    package () {
        abstract type IStatDomain(source = .const(0.0))
        {
            // defined at defs\math\moments.sc: 8.13
            /** Standard deviation
             */
            def StdDev() = Var~>Sqrt
            
            // defined at defs\math\moments.sc: 13.13
            /** Relative standard deviation
             */
            def RelStdDev() = (source-Avg)/StdDev
        }
        
        type Cumulative() : IStatDomain
        {
            // defined at defs\math\moments.sc: 21.13
            /** Cumulative average
             */
            @python.intrinsic("moments.cma.CMA_Impl")
            def Avg() : IDifferentiable
            
            // defined at defs\math\moments.sc: 27.13
            /** Cumulative variance
             */
            @python.intrinsic("moments.cmv.Variance_Impl")
            def Var() : () => Float
        }
        
        @label = "EW_{%(alpha)s}(%(source)s)"
        type EW(alpha = 0.015) : IStatDomain
        {
            // defined at defs\math\moments.sc: 37.13
            /** Exponentially weighted moving average
             */
            @python.intrinsic("moments.ewma.EWMA_Impl")
            def Avg() : IDifferentiable
            
            // defined at defs\math\moments.sc: 43.13
            /** Exponentially weighted moving variance
             */
            @python.intrinsic("moments.ewmv.EWMV_Impl")
            def Var() : () => Float
        }
        
        @label = "Moving_{%(timeframe)s}(%(source)s)"
        type Moving(timeframe = 100.0) : IStatDomain
        {
            // defined at defs\math\moments.sc: 53.13
            /** Simple moving average
             */
            @python.intrinsic("moments.ma.MA_Impl")
            def Avg() : IDifferentiable
            
            // defined at defs\math\moments.sc: 59.13
            /** Simple moving variance
             */
            @python.intrinsic("moments.mv.MV_Impl")
            def Var() : () => Float
        }
    }
}
