
package observable {@category = "Statistics"
    
    package EW {
        @python.intrinsic.function("Statistics", "Avg_{\\alpha=%(alpha)s}(%(source)s)", "moments.ewma.EWMA_Impl")
        @label = "Avg_{\\alpha=%(alpha)s}(%(source)s)"
        def Avg(source = constant(),
                alpha = 0.015) : IDifferentiable
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}", "moments.ewmv.EWMV_Impl")
        @label = "\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}"
        def Var(source = const(),
                alpha = 0.015) : () => Float
            
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}}")
        @label = "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}}"
        def StdDev(source = const(),
                   alpha = 0.015)
             = mathops.Sqrt(Var(source,alpha))
        
        @python.function("Statistics", "RSD_{\\alpha=%(alpha)s}_{%(source)s}")
        @label = "RSD_{\\alpha=%(alpha)s}_{%(source)s}"
        def RelStdDev(source = const(),
                      alpha = 0.15)
             = (source-Avg(source,alpha))/StdDev(source,alpha)
    }
    @category = "Statistics"
    
    package Cumulative {
        @python.intrinsic.function("Statistics", "Avg_{cumul}(%(source)s)", "moments.cma.CMA_Impl")
        @label = "Avg_{cumul}(%(source)s)"
        def Avg(source = const()) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{cumul}(%(source)s)", "moments.cmv.Variance_Impl")
        @label = "\\sigma^2_{cumul}(%(source)s)"
        def Var(source = const()) : () => Float
            
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{cumul}_{%(source)s}}")
        @label = "\\sqrt{\\sigma^2_{cumul}_{%(source)s}}"
        def StdDev(source = const())
             = mathops.Sqrt(Var(source))
        
        @python.function("Statistics", "RSD_{cumul}_{%(source)s}")
        @label = "RSD_{cumul}_{%(source)s}"
        def RelStdDev(source = const())
             = (source-Avg(source))/StdDev(source)
    }
    @category = "Statistics"
    
    package Moving {
        @python.intrinsic.function("Statistics", "Avg_{n=%(timeframe)s}(%(source)s)", "moments.ma.MA_Impl")
        @label = "Avg_{n=%(timeframe)s}(%(source)s)"
        def Avg(source = const(),
                timeframe = 100.0) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{n=%(timeframe)s}(%(source)s)", "moments.mv.MV_Impl")
        @label = "\\sigma^2_{n=%(timeframe)s}(%(source)s)"
        def Var(source = const(),
                timeframe = 100.0)
             = Max(const(0.0),Avg(source*source,timeframe)-Sqr(Avg(source,timeframe)))
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{n=%(timeframe)s}_{%(source)s}}")
        @label = "\\sqrt{\\sigma^2_{n=%(timeframe)s}_{%(source)s}}"
        def StdDev(source = const(),
                   timeframe = 100.0)
             = mathops.Sqrt(Var(source))
        
        @python.function("Statistics", "RSD_{n=%(timeframe)s}_{%(source)s}")
        @label = "RSD_{n=%(timeframe)s}_{%(source)s}"
        def RelStdDev(source = const(),
                      timeframe = 100.0)
             = (source-Avg(source,timeframe))/StdDev(source,timeframe)
    }
}
