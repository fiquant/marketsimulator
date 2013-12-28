@category = "MACD"

package observable.macd {
    @python()
    @label = "MACD_{%(fast)s}^{%(slow)s}(%(x)s)"
    def MACD(x = const(),
             slow = 26.0,
             fast = 12.0)
         = EW.Avg(x,2.0/(fast+1))-EW.Avg(x,2.0/(slow+1))
    
    @python()
    @label = "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))"
    def Signal(x = const(),
               slow = 26.0,
               fast = 12.0,
               timeframe = 9.0,
               step = 1.0)
         = EW.Avg(OnEveryDt(step,MACD(x,slow,fast)),2/(timeframe+1))
    
    @python()
    @label = "Histogram^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))"
    def Histogram(x = const(),
                  slow = 26.0,
                  fast = 12.0,
                  timeframe = 9.0,
                  step = 1.0)
         = MACD(x,slow,fast)-Signal(x,slow,fast,timeframe,step)
}
