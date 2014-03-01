
package math() {@category = "Statistics"
    
    package () {
        // defined at defs\math\moments.sc: 6.9
        /** Exponentially weighted moving average
         */
        @python.intrinsic("moments.ewma.EWMA_Impl")
        def Avg(x = EW()) : IDifferentiable
        
        // defined at defs\math\moments.sc: 12.9
        /** Cumulative average
         */
        @python.intrinsic("moments.cma.CMA_Impl")
        def Avg(x = Cumulative()) : IDifferentiable
        
        // defined at defs\math\moments.sc: 18.9
        /** Simple moving average
         */
        @python.intrinsic("moments.ma.MA_Impl")
        def Avg(x = Moving()) : IDifferentiable
        
        // defined at defs\math\moments.sc: 24.9
        /** Exponentially weighted moving variance
         */
        @python.intrinsic("moments.ewmv.EWMV_Impl")
        def Var(x = EW()) : () => Float
        
        // defined at defs\math\moments.sc: 30.9
        /** Cumulative variance
         */
        @python.intrinsic("moments.cmv.Variance_Impl")
        def Var(x = Cumulative()) : () => Float
        
        // defined at defs\math\moments.sc: 36.9
        /** Simple moving variance
         */
        @python.intrinsic("moments.mv.MV_Impl")
        def Var(x = Moving()) : () => Float
        
        // defined at defs\math\moments.sc: 42.9
        /** Exponentially weighted moving standard deviation
         */
        def StdDev(x = EW()) = x~>Var~>Sqrt
        
        // defined at defs\math\moments.sc: 47.9
        /** Cumulative standard deviation
         */
        def StdDev(x = Cumulative()) = x~>Var~>Sqrt
        
        // defined at defs\math\moments.sc: 52.9
        /** Simple moving standard deviation
         */
        def StdDev(x = Moving()) = x~>Var~>Sqrt
        
        // defined at defs\math\moments.sc: 57.9
        /** Exponentially weighted moving relative standard deviation
         */
        def RelStdDev(x = EW()) = (x~>Source-x~>Avg)/x~>StdDev
        
        // defined at defs\math\moments.sc: 62.9
        /** Cumulative relative standard deviation
         */
        def RelStdDev(x = Cumulative()) = (x~>Source-x~>Avg)/x~>StdDev
        
        // defined at defs\math\moments.sc: 67.9
        /** Simple moving relative standard deviation
         */
        def RelStdDev(x = Moving()) = (x~>Source-x~>Avg)/x~>StdDev
    }
}
