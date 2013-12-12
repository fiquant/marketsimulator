
package observable.macd {
    def MACD(x = orderbook.MidPrice(),
             slow = 26.0,
             fast = 12.0)
         = EWMA(x,2.0/(fast+1.0))-EWMA(x,2.0/(slow+1.0))
    
    def Signal(x = orderbook.MidPrice(),
               slow = 26.0,
               fast = 12.0,
               timeframe = 9.0,
               step = 1.0)
         = EWMA(OnEveryDt(step,MACD(x,slow,fast)),2.0/(timeframe+1.0))
    
    def Histogram(x = orderbook.MidPrice(),
                  slow = 26.0,
                  fast = 12.0,
                  timeframe = 9.0,
                  step = 1.0)
         = MACD(x,slow,fast)-Signal(x,slow,fast,timeframe,step)
}
