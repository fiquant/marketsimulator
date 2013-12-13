package observable
{
    @python.intrinsic.observable("Basic", "Lagged_{%(timeframe)s}(%(source)s)", "observable.lagged.Lagged_Impl")
    def Lagged (source = const (), timeframe = 10) : IObservable

    @python.observable("RSI", "Ups_{%(timeframe)s}(%(source)s)")
    def UpMovements(source = orderbook.MidPrice(), timeframe = 10)
        = Max(const(0), source - Lagged(source, timeframe))

    @python.observable("RSI", "Downs_{%(timeframe)s}(%(source)s)")
    def DownMovements(source = orderbook.MidPrice(), timeframe = 10)
        = Max(const(0), Lagged(source, timeframe) - source)

    package rsi
    {
        @python.observable("RSI", "RSI-raw_{%(timeframe)s}^{%(alpha)s}(%(source)s)")
        def Raw(source = orderbook.MidPrice(), timeframe = 10, alpha = 0.015)
            =   EW.Avg(UpMovements  (source, timeframe), alpha) /
                EW.Avg(DownMovements(source, timeframe), alpha)
    }

    @python.observable("RSI", "RSI_{%(timeframe)s}^{%(alpha)s}(%(book)s)")
    def RSI(book = orderbook.OfTrader(), timeframe = 10, alpha = 0.015)
        = 100.0 - 100.0 / (1.0 + rsi.Raw(orderbook.MidPrice(book), timeframe, alpha))


}