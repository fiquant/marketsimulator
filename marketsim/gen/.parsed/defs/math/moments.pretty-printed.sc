
package math() {@category = "Statistics"
    
    package () {
        abstract type IStatDomain(source = .const(0.0))
        
        type Cumulative() : IStatDomain
        {
            // defined at defs\math\moments.sc: 10.13
            /** Cumulative average
             */
            @python.intrinsic("moments.cma.CMA_Impl")
            def Avg() : IDifferentiable
            
            // defined at defs\math\moments.sc: 16.13
            /** Cumulative variance
             */
            @python.intrinsic("moments.cmv.Variance_Impl")
            def Var() : () => Float
            
            // defined at defs\math\moments.sc: 22.13
            /** Cumulative standard deviation
             */
            def StdDev() = Var~>Sqrt
            
            // defined at defs\math\moments.sc: 27.13
            /** Cumulative relative standard deviation
             */
            def RelStdDev() = (source-Avg)/StdDev
        }
        
        @label = "EW_{%(alpha)s}(%(source)s)"
        type EW(alpha = 0.015) : IStatDomain
        {
            // defined at defs\math\moments.sc: 36.13
            /** Exponentially weighted moving average
             */
            @python.intrinsic("moments.ewma.EWMA_Impl")
            def Avg() : IDifferentiable
            
            // defined at defs\math\moments.sc: 42.13
            /** Exponentially weighted moving variance
             */
            @python.intrinsic("moments.ewmv.EWMV_Impl")
            def Var() : () => Float
            
            // defined at defs\math\moments.sc: 48.13
            /** Exponentially weighted moving standard deviation
             */
            def StdDev() = Var~>Sqrt
            
            // defined at defs\math\moments.sc: 53.13
            /** Exponentially weighted moving relative standard deviation
             */
            def RelStdDev() = (source-Avg)/StdDev
        }
        
        @label = "Moving_{%(timeframe)s}(%(source)s)"
        type Moving(timeframe = 100.0) : IStatDomain
        {
            // defined at defs\math\moments.sc: 62.13
            /** Simple moving average
             */
            @python.intrinsic("moments.ma.MA_Impl")
            def Avg() : IDifferentiable
            
            // defined at defs\math\moments.sc: 68.13
            /** Simple moving variance
             */
            @python.intrinsic("moments.mv.MV_Impl")
            def Var() : () => Float
            
            // defined at defs\math\moments.sc: 74.13
            /** Simple moving standard deviation
             */
            def StdDev() = Var~>Sqrt
            
            // defined at defs\math\moments.sc: 79.13
            /** Simple moving relative standard deviation
             */
            def RelStdDev() = (source-Avg)/StdDev
        }
    }
}
