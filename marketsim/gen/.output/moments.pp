
package observable {
    package EW {
        @python.intrinsic.function("Statistics", "Avg_{\\alpha=%(alpha)s}(%(source)s)", "moments.ewma.EWMA_Impl")
        def Avg(source = const(),
                alpha = 0.015) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}", "moments.ewmv.EWMV_Impl")
        def Var(source = const(),
                alpha = 0.015) : () => Float
            
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{\\alpha=%(alpha)s}_{%(source)s}}")
        def StdDev(source = const(),
                   alpha = 0.015)
             = mathops.Sqrt(Var(source,alpha))
    }
    
    package Cumulative {
        @python.intrinsic.function("Statistics", "Avg_{cumul}(%(source)s)", "moments.cma.CMA_Impl")
        def Avg(source = const()) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2_{cumul}(%(source)s)", "moments.cmv.Variance_Impl")
        def Var(source = const()) : () => Float
            
        
        @python.function("Statistics", "\\sqrt{\\sigma^2_{cumul}_{%(source)s}}")
        def StdDev(source = const())
             = mathops.Sqrt(Var(source))
    }
    
    package Moving {
        @python.intrinsic.function("Statistics", "Avg_{n=%(timeframe)s}(%(source)s)", "moments.ma.MA_Impl")
        def Avg(source = const(),
                timeframe = 100.0) : () => Float
            
    }
}
