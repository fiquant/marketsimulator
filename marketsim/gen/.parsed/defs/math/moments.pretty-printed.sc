
package math() {@category = "Statistics"
    
    package () {
        type IStatDomain(source = .const(0.0))
        
        type Cumulative() : IStatDomain
        
        @label = "EW_{%(alpha)s}(%(source)s)"
        type EW(alpha = 0.015) : IStatDomain
        {
            // defined at defs\math\moments.sc: 13.13
            /** Exponentially weighted moving relative standard deviation
             */
            def RelStdDev() = (source-Avg)/StdDev
        }
        
        @label = "Moving_{%(timeframe)s}(%(source)s)"
        type Moving(timeframe = 100.0) : IStatDomain
        
        // defined at defs\math\moments.sc: 22.9
        /** Exponentially weighted moving average
         */
        @python.intrinsic("moments.ewma.EWMA_Impl")
        def Avg(x = EW()) : IDifferentiable
        
        // defined at defs\math\moments.sc: 28.9
        /** Cumulative average
         */
        @python.intrinsic("moments.cma.CMA_Impl")
        def Avg(x = Cumulative()) : IDifferentiable
        
        // defined at defs\math\moments.sc: 34.9
        /** Simple moving average
         */
        @python.intrinsic("moments.ma.MA_Impl")
        def Avg(x = Moving()) : IDifferentiable
        
        // defined at defs\math\moments.sc: 40.9
        /** Exponentially weighted moving variance
         */
        @python.intrinsic("moments.ewmv.EWMV_Impl")
        def Var(x = EW()) : () => Float
        
        // defined at defs\math\moments.sc: 46.9
        /** Cumulative variance
         */
        @python.intrinsic("moments.cmv.Variance_Impl")
        def Var(x = Cumulative()) : () => Float
        
        // defined at defs\math\moments.sc: 52.9
        /** Simple moving variance
         */
        @python.intrinsic("moments.mv.MV_Impl")
        def Var(x = Moving()) : () => Float
        
        // defined at defs\math\moments.sc: 58.9
        /** Exponentially weighted moving standard deviation
         */
        def StdDev(x = EW()) = x~>Var~>Sqrt
        
        // defined at defs\math\moments.sc: 63.9
        /** Cumulative standard deviation
         */
        def StdDev(x = Cumulative()) = x~>Var~>Sqrt
        
        // defined at defs\math\moments.sc: 68.9
        /** Simple moving standard deviation
         */
        def StdDev(x = Moving()) = x~>Var~>Sqrt
        
        // defined at defs\math\moments.sc: 73.9
        /** Exponentially weighted moving relative standard deviation
         */
        def RelStdDev(x = EW()) = (x~>Source-x~>Avg)/x~>StdDev
        
        // defined at defs\math\moments.sc: 78.9
        /** Cumulative relative standard deviation
         */
        def RelStdDev(x = Cumulative()) = (x~>Source-x~>Avg)/x~>StdDev
        
        // defined at defs\math\moments.sc: 83.9
        /** Simple moving relative standard deviation
         */
        def RelStdDev(x = Moving()) = (x~>Source-x~>Avg)/x~>StdDev
    }
}
