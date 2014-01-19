
package observable() {@category = "Statistics"
    
    package () {@suffix = "_{\\\\alpha=%(alpha)s}(%(source)s)"
        
        package EW(source = const(),alpha = 0.015) {
            @python.intrinsic("moments.ewma.EWMA_Impl")
            @label = "Avg{{suffix}}"
            def Avg(source = const(),
                    alpha = 0.015) : IDifferentiable
                
            
            @python.intrinsic("moments.ewmv.EWMV_Impl")
            @label = "\\sigma^2{{suffix}}"
            def Var(source = const(),
                    alpha = 0.015) : () => Float
                
            
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev(source = const(),
                       alpha = 0.015)
                 = mathops.Sqrt(Var(source,alpha))
            
            @label = "RSD{{suffix}}"
            def RelStdDev(source = const(),
                          alpha = 0.15)
                 = (source-Avg(source,alpha))/StdDev(source,alpha)
        }
        @suffix = "_{cumul}(%(source)s)"
        
        package Cumulative(source = const()) {
            @python.intrinsic("moments.cma.CMA_Impl")
            @label = "Avg{{suffix}}"
            def Avg(source = const()) : () => Float
                
            
            @python.intrinsic("moments.cmv.Variance_Impl")
            @label = "\\sigma^2{{suffix}}"
            def Var(source = const()) : () => Float
                
            
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev(source = const())
                 = mathops.Sqrt(Var(source))
            
            @label = "RSD{{suffix}}"
            def RelStdDev(source = const())
                 = (source-Avg(source))/StdDev(source)
        }
        @suffix = "_{n=%(timeframe)s}(%(source)s)"
        
        package Moving(source = const(),timeframe = 100.0) {
            @python.intrinsic("moments.ma.MA_Impl")
            @label = "Avg{{suffix}}"
            def Avg(source = const(),
                    timeframe = 100.0) : () => Float
                
            
            @python.intrinsic("moments.mv.MV_Impl")
            @label = "\\sigma^2{{suffix}}"
            def Var(source = const(),
                    timeframe = 100.0)
                 = observable.Max(const(0),Avg(source*source,timeframe)-Sqr(Avg(source,timeframe)))
            
            @label = "\\sqrt{\\sigma^2{{suffix}}}"
            def StdDev(source = const(),
                       timeframe = 100.0)
                 = mathops.Sqrt(Var(source))
            
            @label = "RSD{{suffix}}"
            def RelStdDev(source = const(),
                          timeframe = 100.0)
                 = (source-Avg(source,timeframe))/StdDev(source,timeframe)
        }
    }
}
