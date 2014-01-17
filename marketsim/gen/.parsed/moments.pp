
package observable {@category = "Statistics"
    
    package  {
        package EW {
            @python.intrinsic("moments.ewma.EWMA_Impl")
            @label = "Avg_{\\alpha=%(alpha)s}(%(source)s)"
            def Avg(source = const(),
                    alpha = 0.015) : IDifferentiable
                
            
            @python.intrinsic("moments.ewmv.EWMV_Impl")
            @label = "\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}"
            def Var(source = const(),
                    alpha = 0.015) : () => Float
                
            
            @label = "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}}"
            def StdDev(source = const(),
                       alpha = 0.015)
                 = mathops.Sqrt(Var(source,alpha))
            
            @label = "RSD_{\\alpha=%(alpha)s}_{%(source)s}"
            def RelStdDev(source = const(),
                          alpha = 0.15)
                 = (source-Avg(source,alpha))/StdDev(source,alpha)
        }
        
        package Cumulative {
            @python.intrinsic("moments.cma.CMA_Impl")
            @label = "Avg_{cumul}(%(source)s)"
            def Avg(source = const()) : () => Float
                
            
            @python.intrinsic("moments.cmv.Variance_Impl")
            @label = "\\sigma^2_{cumul}(%(source)s)"
            def Var(source = const()) : () => Float
                
            
            @label = "\\sqrt{\\sigma^2_{cumul}_{%(source)s}}"
            def StdDev(source = const())
                 = mathops.Sqrt(Var(source))
            
            @label = "RSD_{cumul}_{%(source)s}"
            def RelStdDev(source = const())
                 = (source-Avg(source))/StdDev(source)
        }
        
        package Moving {
            @python.intrinsic("moments.ma.MA_Impl")
            @label = "Avg_{n=%(timeframe)s}(%(source)s)"
            def Avg(source = const(),
                    timeframe = 100.0) : () => Float
                
            
            @python.intrinsic("moments.mv.MV_Impl")
            @label = "\\sigma^2_{n=%(timeframe)s}(%(source)s)"
            def Var(source = const(),
                    timeframe = 100.0)
                 = observable.Max(const(0),Avg(source*source,timeframe)-Sqr(Avg(source,timeframe)))
            
            @label = "\\sqrt{\\sigma^2_{n=%(timeframe)s}_{%(source)s}}"
            def StdDev(source = const(),
                       timeframe = 100.0)
                 = mathops.Sqrt(Var(source))
            
            @label = "RSD_{n=%(timeframe)s}_{%(source)s}"
            def RelStdDev(source = const(),
                          timeframe = 100.0)
                 = (source-Avg(source,timeframe))/StdDev(source,timeframe)
        }
    }
}
