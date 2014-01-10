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


