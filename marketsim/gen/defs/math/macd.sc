package math
{
    @category = "MACD"
    package {
        @label = "MACD_{%(fast)s}^{%(slow)s}(%(source)s)"
        type macd(/** source */       source = .const(1.),
                  /** long period */  slow = 26.0,
                  /** short period */ fast = 12.0)
        {
            /**
             *  Moving average convergence/divergence
             */
            def Value = source~>EW(2./(fast+1))~>Avg - source~>EW(2./(slow+1))~>Avg

            /**
             *  Moving average convergence/divergence signal
             */
            @label = "Signal^{%(timeframe)s}_{%(step)s}(%(x)s)"
            def Signal(/** signal period */         timeframe = 9.0,
                       /** discretization step */   step = 1.0)

                = Value~>OnEveryDt(step)~>EW(2/(timeframe+1))~>Avg

            /**
             *  Moving average convergence/divergence histogram
             */
            @label = "Histogram^{%(timeframe)s}_{%(step)s}(%(x)s)"
            def Histogram(  /** signal period */         timeframe = 9.0,
                            /** discretization step */   step = 1.0)

                = Value - Signal(timeframe, step)
        }
    }
}