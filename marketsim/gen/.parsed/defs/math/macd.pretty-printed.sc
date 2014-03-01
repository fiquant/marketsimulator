
package math() {@category = "MACD"
    
    package () {
        @label = "MACD_{%(fast)s}^{%(slow)s}(%(source)s)"
        type macd(/** source */ source = .const(1.0),/** long period */ slow = 26.0,/** short period */ fast = 12.0)
        
        // defined at defs\math\macd.sc: 9.9
        /** Moving average convergence/divergence
         */
        def Value(x = macd()) = x~>Source~>EW(2.0/(x~>Fast+1))~>Avg-x~>Source~>EW(2.0/(x~>Slow+1))~>Avg
        
        // defined at defs\math\macd.sc: 16.9
        /** Moving average convergence/divergence signal
         */
        @label = "Signal^{%(timeframe)s}_{%(step)s}(%(x)s)"
        def Signal(x = macd(),
                   /** signal period */ timeframe = 9.0,
                   /** discretization step */ step = 1.0) = x~>Value~>OnEveryDt(step)~>EW(2/(timeframe+1))~>Avg
        
        // defined at defs\math\macd.sc: 26.9
        /** Moving average convergence/divergence histogram
         */
        @label = "Histogram^{%(timeframe)s}_{%(step)s}(%(x)s)"
        def Histogram(x = macd(),
                      /** signal period */ timeframe = 9.0,
                      /** discretization step */ step = 1.0) = x~>Value-x~>Signal(timeframe,step)
    }
}
