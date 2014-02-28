
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
            @label = "EW_{\\\\alpha=%(alpha)s}"
            def EW(source = const(1.0),
                   alpha = 0.015) : IEW
            
            // defined at defs\math\moments.sc: 138.13
            @python.intrinsic.function("_constant._Empty_Impl")
            def Cumulative(source = const(1.0)) : ICumulative
            
            // defined at defs\math\moments.sc: 141.13
            @python.intrinsic.function("_constant._Empty_Impl")
            @label = "Moving_{%(timeframe)s}"
            def Moving(source = const(1.0),
                       timeframe = 100.0) : IMoving
            
            // defined at defs\math\moments.sc: 145.13
            @python.intrinsic("moments.tmp.Source_Impl")
            def Source(x = EW() : IStatDomain) : IObservable[Float]
            
            // defined at defs\math\moments.sc: 148.13
            @python.intrinsic.function("moments.tmp.Alpha_Impl")
            def Alpha(x = EW()) : Float
            
            // defined at defs\math\moments.sc: 151.13
            @python.intrinsic.function("moments.tmp.Timeframe_Impl")
            def Timeframe(x = Moving()) : Float
            
            // defined at defs\math\moments.sc: 154.13
            def Avg(x = EW()) = math.EW.Avg(Source(x),Alpha(x))
            
            // defined at defs\math\moments.sc: 155.13
            def Avg(x = Cumulative()) = math.Cumulative.Avg(Source(x))
            
            // defined at defs\math\moments.sc: 156.13
            def Avg(x = Moving()) = math.Moving.Avg(Source(x),Timeframe(x))
            
            // defined at defs\math\moments.sc: 158.13
            def Var(x = EW()) = math.EW.Var(Source(x),Alpha(x))
            
            // defined at defs\math\moments.sc: 159.13
            def Var(x = Cumulative()) = math.Cumulative.Var(Source(x))
            
            // defined at defs\math\moments.sc: 160.13
            def Var(x = Moving()) = math.Moving.Var(Source(x),Timeframe(x))
            
            // defined at defs\math\moments.sc: 162.13
            def StdDev(x = EW()) = math.EW.StdDev(Source(x),Alpha(x))
            
            // defined at defs\math\moments.sc: 163.13
            def StdDev(x = Cumulative()) = math.Cumulative.StdDev(Source(x))
            
            // defined at defs\math\moments.sc: 164.13
            def StdDev(x = Moving()) = math.Moving.StdDev(Source(x),Timeframe(x))
            
            // defined at defs\math\moments.sc: 166.13
            def RelStdDev(x = EW()) = math.EW.RelStdDev(Source(x),Alpha(x))
            
            // defined at defs\math\moments.sc: 167.13
            def RelStdDev(x = Cumulative()) = math.Cumulative.RelStdDev(Source(x))
            
            // defined at defs\math\moments.sc: 168.13
            def RelStdDev(x = Moving()) = math.Moving.RelStdDev(Source(x),Timeframe(x))
        }
    }
}
