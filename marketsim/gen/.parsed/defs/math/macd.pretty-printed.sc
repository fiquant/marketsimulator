@category = "MACD"

package math.macd {
    // defined at defs\math\macd.sc: 4.5
    /** Moving average convergence/divergence
     */
    @label = "MACD_{%(fast)s}^{%(slow)s}(%(x)s)"
    def MACD(/** source */ x = const(),
             /** long period */ slow = 26.0,
             /** short period */ fast = 12.0) = EW.Avg(x,2.0/(fast+1))-EW.Avg(x,2.0/(slow+1))
    
    // defined at defs\math\macd.sc: 14.5
    /** Moving average convergence/divergence signal
     */
    @label = "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))"
    def Signal(/** source */ x = const(),
               /** long period */ slow = 26.0,
               /** short period */ fast = 12.0,
               /** signal period */ timeframe = 9.0,
               /** discretization step */ step = 1.0) = EW.Avg(observable.OnEveryDt(step,MACD(x,slow,fast)),2/(timeframe+1))
    
    // defined at defs\math\macd.sc: 26.5
    /** Moving average convergence/divergence histogram
     */
    @label = "Histogram^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))"
    def Histogram(/** source */ x = const(),
                  /** long period */ slow = 26.0,
                  /** short period */ fast = 12.0,
                  /** signal period */ timeframe = 9.0,
                  /** discretization step */ step = 1.0) = MACD(x,slow,fast)-Signal(x,slow,fast,timeframe,step)
}
