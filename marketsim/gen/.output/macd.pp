
package observable.macd {
    @python.function("MACD", "MACD_{%(fast)s}^{%(slow)s}(%(x)s)")
    def MACD(x = orderbook.MidPrice(),
             slow = 26.0,
             fast = 12.0)
         = EW.Avg(x,2.0/(fast+1.0))-EW.Avg(x,2.0/(slow+1.0))
    
    @python.function("MACD", "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))")
    def Signal(x = orderbook.MidPrice(),
               slow = 26.0,
               fast = 12.0,
               timeframe = 9.0,
               step = 1.0)
         = EW.Avg(OnEveryDt(step,MACD(x,slow,fast)),2.0/(timeframe+1.0))
    
    @python.function("MACD", "Histogram^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))")
    def Histogram(x = orderbook.MidPrice(),
                  slow = 26.0,
                  fast = 12.0,
                  timeframe = 9.0,
                  step = 1.0)
         = MACD(x,slow,fast)-Signal(x,slow,fast,timeframe,step)
}
