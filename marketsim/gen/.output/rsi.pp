
package observable {
    @python.intrinsic("observable.lagged.Lagged_Impl")
    @label = "Lagged_{%(timeframe)s}(%(source)s)"
    def Lagged(source = const(),
               timeframe = 10.0) : IObservable[Float]
        
    
    @python.observable()
    @label = "Ups_{%(timeframe)s}(%(source)s)"
    def UpMovements(source = orderbook.MidPrice(),
                    timeframe = 10.0)
         = Observable(Max(const(0.0),source-Lagged(source,timeframe)))
    
    @python.observable()
    @label = "Downs_{%(timeframe)s}(%(source)s)"
    def DownMovements(source = orderbook.MidPrice(),
                      timeframe = 10.0)
         = Observable(Max(const(0.0),Lagged(source,timeframe)-source))
    @category = "RSI"
    
    package rsi {
        @python()
        @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
        def Raw(source = orderbook.MidPrice(),
                timeframe = 10.0,
                alpha = 0.015)
             = EW.Avg(UpMovements(source,timeframe),alpha)/EW.Avg(DownMovements(source,timeframe),alpha)
    }
    
    @python()
    @label = "RSI_{%(timeframe)s}^{%(alpha)s}(%(book)s)"
    def RSI(book = orderbook.OfTrader(),
            timeframe = 10.0,
            alpha = 0.015)
         = 100.0-100.0/(1.0+rsi.Raw(orderbook.MidPrice(book),timeframe,alpha))
}
