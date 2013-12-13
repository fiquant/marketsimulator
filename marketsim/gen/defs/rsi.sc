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
}