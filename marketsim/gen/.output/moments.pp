
package observable {
    package EW {
        @python.intrinsic.function("Statistics", "Avg_{\\alpha=%(alpha)s}(%(source)s)", "moments.ewma.EWMA_Impl")
        def Avg(source = const(),
                alpha = 0.015) : () => Float
            
        
        @python.intrinsic.function("Statistics", "\\sigma^2^{\\alpha=%(alpha)s}_{%(source)s}", "moments.ewmv.EWMV_Impl")
        def Var(source = const(),
                alpha = 0.015) : () => Float
            
    }
}
