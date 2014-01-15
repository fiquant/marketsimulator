@category = "Basic"
package observable
{
    @python.observable
    @category = "Pow/Log"
    @label = "{%(x)s}^2"
    def Sqr(x = constant()) = x*x

    @python.observable
    @label = "min{%(x)s, %(y)s}"
    def Min(x = constant(), y = constant()) = if x < y then x else y

    @python.observable
    @label = "max{%(x)s, %(y)s}"
    def Max(x = constant(), y = constant()) = if x > y then x else y

    @python.intrinsic("observable.on_every_dt._OnEveryDt_Impl")
    @label = "[%(x)s]_dt=%(dt)s"
    @observe_args = "no"
    def OnEveryDt(dt = 1.0, x = constant()) : IObservable[Float]

    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    @label = "[%(x)s]"
    def Observable(x = const() : IFunction[Float]) : IObservable[Float]

    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    @label = "[%(x)s]"
    def ObservablePrice(x = const() : IFunction[Float]) : IObservable[Price]

    @python.intrinsic("observable.on_every_dt._Observable_Impl")
    @label = "[%(x)s]"
    def ObservableVolume(x = const() : IFunction[Float]) : IObservable[Volume]

    @python.intrinsic("observable.on_every_dt._ObservableSide_Impl")
    @label = "[%(x)s]"
    def ObservableSide(x = side.Sell() : IFunction[Side]) : IObservable[Side]

    @python.intrinsic("observable.quote.Quote_Impl")
    @label = "%(ticker)s"
    def Quote(ticker = "^GSPC", start = "2001-1-1", end = "2010-1-1") : IObservable[Price]

    @python.intrinsic("observable.breaks_at_changes._BreaksAtChanges_Impl")
    def BreaksAtChanges(source = constant(1.)) : IObservable[Float]

    @python.intrinsic("observable.candlestick.CandleSticks_Impl")
    def CandleSticks(source = const(), timeframe = 10.0) : IObservable[CandleStick]

    package Moving
    {
        @python.intrinsic("observable.minmax.Min_Impl")
        @label = "Min_{n=%(timeframe)s}(%(source)s)"
        def Min(source = constant(), timeframe = 100.) : IObservable[Float]

        @python.intrinsic("observable.minmax.Max_Impl")
        @label = "Max_{n=%(timeframe)s}(%(source)s)"
        def Max(source = constant(), timeframe = 100.) : IObservable[Float]
    }

    package Cumulative
    {
        @python.intrinsic("observable.minmax_eps.MinEpsilon_Impl")
        @label = "Min_{\\epsilon}(%(source)s)"
        def MinEpsilon(source = constant(), epsilon = constant(0.01)) : IObservable[Float]

        @python.intrinsic("observable.minmax_eps.MaxEpsilon_Impl")
        @label = "Max_{\\epsilon}(%(source)s)"
        def MaxEpsilon(source = constant(), epsilon = constant(0.01)) : IObservable[Float]
    }
}

@category = "Basic"
package {
    @label = "C=%(x)s"
    def constant(x = 1.0) : IFunction[Float] = const(x)

    @python.intrinsic.function("_constant._Constant_Impl")
    @label = "C=%(x)s"
    def const(x = 1.0) : IObservable[Float]

    @python.intrinsic.function("_constant._True_Impl")
    @label = "True"
    def true() : IObservable[Boolean]

    @python.intrinsic.function("_constant._False_Impl")
    @label = "False"
    def false() : IObservable[Boolean]

    @python.intrinsic("_constant._Null_Impl")
    def null() => Float

    @python.observable
    @label = "If def(%(x)s) else %(elsePart)s"
    def IfDefined(x = constant(), elsePart = constant()) =
        if x <> null() then x else elsePart

    def EWMA = observable.EW.Avg

    @python.intrinsic("observable.derivative._Derivative_Impl")
    @label = "\\frac{d%(x)s}{dt}"
    def Derivative(x = EWMA() : IDifferentiable) => Float

    @python.intrinsic("timeserie._ToRecord_Impl")
    @label = "%(source)s"
    def TimeSerie(source        = const(0.) : IObservable[Any],
                  graph         = veusz.Graph(),
                  _digitsToShow = 4) : ITimeSerie

    @python.intrinsic("timeserie._VolumeLevels_Impl")
    @label = "%(source)s"
    def volumeLevels(source        = const(0.) : IObservable[Any],
                     graph         = veusz.Graph(),
                     _digitsToShow = 4) : ITimeSerie
}

@category = "Trader"
package trader
{
    /**
     * A trader that trades a single asset on a single market
     */
    @python.intrinsic("trader.classes._SingleAsset_Impl")
    @label = "%(name)s"
    def SingleAsset(/** order book for the asset being traded */
                    orderBook : IOrderBook,
                    /** strategy run by the trader */
                    strategy    = strategy.Noise(),
                    name        = "-trader-",
                    /** current position of the trader (number of assets that it owns) */
                    amount      = 0.0,
                    /** current trader balance (number of money units that it owns) */
                    PnL         = 0.0,
                    timeseries  = [] : List[ITimeSerie]) : ISingleAssetTrader

    @python.intrinsic("trader.classes._MultiAsset_Impl")
    @label = "%(name)s"
    def MultiAsset( traders     = [] : List[ISingleAssetTrader],
                    /** strategy run by the trader */
                    strategy    = strategy.Arbitrage(),
                    name        = "-trader-",
                    /** current trader balance (number of money units that it owns) */
                    PnL         = 0.0,
                    timeseries  = [] : List[ITimeSerie]) : ITrader
}

@category = "Side"
package side
{
    @python.intrinsic("side._Sell_Impl")
    def Sell() => Side

    @python.intrinsic("side._Buy_Impl")
    def Buy() => Side

    @python.intrinsic("side._Buy_Impl")
    def Nothing() => Side
}

@category = "Event"
package event
{
    @python.intrinsic("event._Every_Impl")
    def Every(intervalFunc = mathutils.rnd.expovariate(1.)) : IEvent

    @python.intrinsic("event._After_Impl")
    def After(delay = constant(10.)) : IEvent
}

@category = "N/A"
package veusz
{
    @python.intrinsic("veusz._Graph_Impl")
    def Graph(name = "graph") : IGraph
}


