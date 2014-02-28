
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
                    /** sliding window size    */ timeframe = 100.0) = source~>Sqr~>Moving_Avg(timeframe)-source~>Moving_Avg(timeframe)~>Sqr~>Max(0)
            
            // defined at defs\math\moments.sc: 106.13
            /** Simple moving standard deviation
             */
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            @method = "{{kind}}_StdDev"
            def StdDev(/** observable data source */ source = const(1.0),
                       /** sliding window size    */ timeframe = 100.0) = source~>Moving_Var(timeframe)~>Sqrt
            
            // defined at defs\math\moments.sc: 116.13
            /** Simple moving relative standard deviation
             */
            @label = "RSD{{suffix}}"
            @method = "{{kind}}_RelStdDev"
            def RelStdDev(/** observable data source */ source = const(1.0),
                          /** sliding window size    */ timeframe = 100.0) = (source-source~>Moving_Avg(timeframe))/source~>Moving_StdDev(timeframe)
        }
        
        package impl() {
            type IStatDomain
            
            type IEW : IStatDomain
            
            type ICumulative : IStatDomain
            
            type IMoving : IStatDomain
            
            // defined at defs\math\moments.sc: 134.13
            @python.intrinsic.function("_constant._Empty_Impl")
            def EW(source = const(1.0),
                   alpha = 0.015) : IEW
            
            // defined at defs\math\moments.sc: 137.13
            @python.intrinsic.function("_constant._Empty_Impl")
            def Cumulative(source = const(1.0)) : ICumulative
            
            // defined at defs\math\moments.sc: 140.13
            @python.intrinsic.function("_constant._Empty_Impl")
            def Moving(source = const(1.0),
                       timeframe = 100.0) : IMoving
            
            // defined at defs\math\moments.sc: 143.13
            @python.intrinsic("moments.tmp.Source_Impl")
            @method = "N/A"
            def source(x = EW() : IStatDomain) : IObservable[Float]
            
            // defined at defs\math\moments.sc: 147.13
            @python.intrinsic.function("moments.tmp.Alpha_Impl")
            @method = "N/A"
            def alpha(x = EW()) : Float
            
            // defined at defs\math\moments.sc: 151.13
            @python.intrinsic.function("moments.tmp.Timeframe_Impl")
            @method = "N/A"
            def timeframe(x = Moving()) : Float
        }
    }
}
