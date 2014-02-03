
package math {@category = "Statistics"
    
    package  {@suffix = "_{\\\\alpha=%(alpha)s}(%(source)s)"
        
        package EW {
            // defined at defs\math\moments.sc: 9.13
            /** Exponentially weighted moving average
             */
            @python.intrinsic("moments.ewma.EWMA_Impl")
            @label = "Avg{{suffix}}"
            def Avg(/** observable data source */ source = const(),
                    /** alpha parameter */ alpha = 0.015) : IDifferentiable
            
            // defined at defs\math\moments.sc: 17.13
            /** Exponentially weighted moving variance
             */
            @python.intrinsic("moments.ewmv.EWMV_Impl")
            @label = "\\sigma^2{{suffix}}"
            def Var(/** observable data source */ source = const(),
                    /** alpha parameter */ alpha = 0.015) : () => Float
            
            // defined at defs\math\moments.sc: 24.13
            /** Exponentially weighted moving standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev(/** observable data source */ source = const(),
                       /** alpha parameter */ alpha = 0.015) = Sqrt(Var(source,alpha))
            
            // defined at defs\math\moments.sc: 31.13
            /** Exponentially weighted moving relative standard deviation
             */
            @label = "RSD{{suffix}}"
            def RelStdDev(/** observable data source */ source = const(),
                          /** alpha parameter */ alpha = 0.015) = (source-Avg(source,alpha))/StdDev(source,alpha)
        }
        @suffix = "_{cumul}(%(source)s)"
        
        package Cumulative {
            // defined at defs\math\moments.sc: 43.13
            /** Cumulative average
             */
            @python.intrinsic("moments.cma.CMA_Impl")
            @label = "Avg{{suffix}}"
            def Avg(/** observable data source */ source = const()) : () => Float
            
            // defined at defs\math\moments.sc: 50.13
            /** Cumulative variance
             */
            @python.intrinsic("moments.cmv.Variance_Impl")
            @label = "\\sigma^2{{suffix}}"
            def Var(/** observable data source */ source = const()) : () => Float
            
            // defined at defs\math\moments.sc: 57.13
            /** Cumulative standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev(/** observable data source */ source = const()) = Sqrt(Var(source))
            
            // defined at defs\math\moments.sc: 64.13
            /** Cumulative relative standard deviation
             */
            @label = "RSD{{suffix}}"
            def RelStdDev(/** observable data source */ source = const()) = (source-Avg(source))/StdDev(source)
        }
        @suffix = "_{n=%(timeframe)s}(%(source)s)"
        
        package Moving {
            // defined at defs\math\moments.sc: 75.13
            /** Simple moving average
             */
            @python.intrinsic("moments.ma.MA_Impl")
            @label = "Avg{{suffix}}"
            def Avg(/** observable data source */ source = const(),
                    /** sliding window size    */ timeframe = 100.0) : () => Float
            
            // defined at defs\math\moments.sc: 83.13
            /** Simple moving variance
             */
            @python.intrinsic("moments.mv.MV_Impl")
            @label = "\\sigma^2{{suffix}}"
            def Var(/** observable data source */ source = const(),
                    /** sliding window size    */ timeframe = 100.0) = math.Max(const(0),Avg(observable.Float(source*source),timeframe)-Sqr(Avg(source,timeframe)))
            
            // defined at defs\math\moments.sc: 92.13
            /** Simple moving standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev(/** observable data source */ source = const(),
                       /** sliding window size    */ timeframe = 100.0) = Sqrt(Var(source))
            
            // defined at defs\math\moments.sc: 99.13
            /** Simple moving relative standard deviation
             */
            @label = "RSD{{suffix}}"
            def RelStdDev(/** observable data source */ source = const(),
                          /** sliding window size    */ timeframe = 100.0) = (source-Avg(source,timeframe))/StdDev(source,timeframe)
        }
    }
}
