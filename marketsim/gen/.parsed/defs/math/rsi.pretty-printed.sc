
package math {
    /** Observable that adds a lag to an observable data source so [Lagged(x, dt)]t=t0 == [x]t=t0+dt
     */
    @python.intrinsic("observable.lagged.Lagged_Impl")
    @label = "Lagged_{%(timeframe)s}(%(source)s)"
    def Lagged(/** observable data source */ source = const(),
               /** lag size */ timeframe = 10.0) : IObservable[Float] // defined at defs\math\rsi.sc: 3.5
    
    /** Returns positive movements of some observable *source* with lag *timeframe*
     */
    @label = "Ups_{%(timeframe)s}(%(source)s)"
    def UpMovements(/** observable data source */ source = const(),
                    /** lag size */ timeframe = 10.0) = observable.Float(Max(const(0.0),source-Lagged(source,timeframe))) // defined at defs\math\rsi.sc: 11.5
    
    /** Returns negative movements of some observable *source* with lag *timeframe*
     */
    @label = "Downs_{%(timeframe)s}(%(source)s)"
    def DownMovements(/** observable data source */ source = const(),
                      /** lag size */ timeframe = 10.0) = observable.Float(Max(const(0.0),Lagged(source,timeframe)-source)) // defined at defs\math\rsi.sc: 20.5
    @category = "RSI"
    
    package rsi {
        /** Absolute value for Relative Strength Index
         */
        @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
        def Raw(/** observable data source */ source = const(),
                /** lag size */ timeframe = 10.0,
                /** alpha parameter for EWMA */ alpha = 0.015) = EW.Avg(UpMovements(source,timeframe),alpha)/EW.Avg(DownMovements(source,timeframe),alpha) // defined at defs\math\rsi.sc: 32.9
    }
    
    /** Relative Strength Index
     */
    @label = "RSI_{%(timeframe)s}^{%(alpha)s}(%(book)s)"
    def RSI(/** asset price in question  */ book = orderbook.OfTrader(),
            /** lag size */ timeframe = 10.0,
            /** alpha parameter for EWMA */ alpha = 0.015) = 100.0-100.0/(1.0+rsi.Raw(orderbook.MidPrice(book),timeframe,alpha)) // defined at defs\math\rsi.sc: 44.5
    
    /** Log returns
     */
    @label = "LogReturns_{%(timeframe)s}(%(x)s)"
    def LogReturns(/** observable data source */ x = const(),
                   /** lag size */ timeframe = 10.0) = Log(x/Lagged(x,timeframe)) // defined at defs\math\rsi.sc: 54.5
}
