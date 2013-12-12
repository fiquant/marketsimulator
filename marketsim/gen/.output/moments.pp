
package observable {
    package EW {
        @python.intrinsic.function("Statistics", "Avg_{\\alpha=%(alpha)s}(%(source)s)", "observable.ewma.EWMA_Impl")
        def Avg(source = const(),
                alpha = 0.015) : () => Float
            
    }
}
