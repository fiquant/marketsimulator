
package math() {@category = "Statistics"
    
    package () {@suffix = "_{\\\\alpha=%(alpha)s}(%(source)s)"
        @kind = "EW"
        
        package EW() {
            // defined at defs\math\moments.sc: 10.13
            /** Exponentially weighted moving average
             */
            @python.intrinsic("moments.ewma.EWMA_Impl")
            @label = "Avg{{suffix}}"
            @method = "{{kind}}_Avg"
            def Avg(/** observable data source */ source = const(1.0),
                    /** alpha parameter */ alpha = 0.015) : IDifferentiable
            
            // defined at defs\math\moments.sc: 19.13
            /** Exponentially weighted moving variance
             */
            @python.intrinsic("moments.ewmv.EWMV_Impl")
            @label = "\\sigma^2{{suffix}}"
            @method = "{{kind}}_Var"
            def Var(/** observable data source */ source = const(1.0),
                    /** alpha parameter */ alpha = 0.015) : () => Float
            
            // defined at defs\math\moments.sc: 27.13
            /** Exponentially weighted moving standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            @method = "{{kind}}_StdDev"
            def StdDev(/** observable data source */ source = const(1.0),
                       /** alpha parameter */ alpha = 0.015) = source~>EW_Var(alpha)~>Sqrt
            
            // defined at defs\math\moments.sc: 35.13
            /** Exponentially weighted moving relative standard deviation
             */
            @label = "RSD{{suffix}}"
            @method = "{{kind}}_RelStdDev"
            def RelStdDev(/** observable data source */ source = const(1.0),
                          /** alpha parameter */ alpha = 0.015) = (source-source~>EW_Avg(alpha))/source~>EW_StdDev(alpha)
        }
        @suffix = "_{cumul}(%(source)s)"
        @kind = "Cumulative"
        
        package Cumulative() {
            // defined at defs\math\moments.sc: 49.13
            /** Cumulative average
             */
            @python.intrinsic("moments.cma.CMA_Impl")
            @label = "Avg{{suffix}}"
            @method = "{{kind}}_Avg"
            def Avg(/** observable data source */ source = const(1.0)) : IDifferentiable
            
            // defined at defs\math\moments.sc: 57.13
            /** Cumulative variance
             */
            @python.intrinsic("moments.cmv.Variance_Impl")
            @label = "\\sigma^2{{suffix}}"
            @method = "{{kind}}_Var"
            def Var(/** observable data source */ source = const(1.0)) : () => Float
            
            // defined at defs\math\moments.sc: 65.13
            /** Cumulative standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            @method = "{{kind}}_StdDev"
            def StdDev(/** observable data source */ source = const(1.0)) = Sqrt(Var(source))
            
            // defined at defs\math\moments.sc: 73.13
            /** Cumulative relative standard deviation
             */
            @label = "RSD{{suffix}}"
            @method = "{{kind}}_RelStdDev"
            def RelStdDev(/** observable data source */ source = const(1.0)) = (source-Avg(source))/StdDev(source)
        }
        @suffix = "_{n=%(timeframe)s}(%(source)s)"
        @kind = "Moving"
        
        package Moving() {
            // defined at defs\math\moments.sc: 86.13
            /** Simple moving average
             */
            @python.intrinsic("moments.ma.MA_Impl")
            @label = "Avg{{suffix}}"
            @method = "{{kind}}_Avg"
            def Avg(/** observable data source */ source = const(1.0),
                    /** sliding window size    */ timeframe = 100.0) : IDifferentiable
            
            // defined at defs\math\moments.sc: 95.13
            /** Simple moving variance
             */
            @python.intrinsic("moments.mv.MV_Impl")
            @label = "\\sigma^2{{suffix}}"
            @method = "{{kind}}_Var"
            def Var(/** observable data source */ source = const(1.0),
                    /** sliding window size    */ timeframe = 100.0) = math.Max(const(0),Avg(source*source,timeframe)-Sqr(Avg(source,timeframe)))
            
            // defined at defs\math\moments.sc: 105.13
            /** Simple moving standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            @method = "{{kind}}_StdDev"
            def StdDev(/** observable data source */ source = const(1.0),
                       /** sliding window size    */ timeframe = 100.0) = Sqrt(Var(source))
            
            // defined at defs\math\moments.sc: 113.13
            /** Simple moving relative standard deviation
             */
            @label = "RSD{{suffix}}"
            @method = "{{kind}}_RelStdDev"
            def RelStdDev(/** observable data source */ source = const(1.0),
                          /** sliding window size    */ timeframe = 100.0) = (source-Avg(source,timeframe))/StdDev(source,timeframe)
        }
    }
}
