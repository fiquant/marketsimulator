
package observable {
    @python.intrinsic.observable("Basic", "Lagged_{%(timeframe)s}(%(source)s)", "observable.lagged.Lagged_Impl")
    def Lagged(source = const(),
               timeframe = 10.0) : IObservable
        
    
    @python.observable("RSI", "Ups_{%(timeframe)s}(%(source)s)")
    def UpMovements(source = orderbook.MidPrice(),
                    timeframe = 10.0)
         = Max(const(0.0),source-Lagged(source,timeframe))
    
    @python.observable("RSI", "Downs_{%(timeframe)s}(%(source)s)")
    def DownMovements(source = orderbook.MidPrice(),
                      timeframe = 10.0)
         = Max(const(0.0),Lagged(source,timeframe)-source)
    
    package rsi {
        @python.observable("RSI", "RSI-raw_{%(timeframe)s}^{%(alpha)s}(%(source)s)")
        def Raw(source = orderbook.MidPrice(),
                timeframe = 10.0,
                alpha = 0.015)
             = EW.Avg(UpMovements(source,timeframe),alpha)/EW.Avg(DownMovements(source,timeframe),alpha)
    }
}
