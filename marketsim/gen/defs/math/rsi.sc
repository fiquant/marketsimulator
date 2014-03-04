package math
{
    /**
     *  Observable that adds a lag to an observable data source
     *  so Lagged(x, dt)(t0+dt) == x(t0)
     */
    @python.intrinsic("observable.lagged.Lagged_Impl")
    @label = "Lagged_{%(timeframe)s}(%(source)s)"
    def Lagged (/** observable data source */   source    = const (1.),
                /** lag size */                 timeframe = 10.0) : IObservable[Float]

    /**
     *  Returns positive movements of some observable *source* with lag *timeframe*
     */
    @label = "Ups_{%(timeframe)s}(%(source)s)"
    def UpMovements(/** observable data source */   source = const (1.),
                    /** lag size */                 timeframe = 10.0)

        = Max(0.0, source - source~>Lagged(timeframe))

    /**
     *  Returns negative movements of some observable *source* with lag *timeframe*
     */
    @label = "Downs_{%(timeframe)s}(%(source)s)"
    def DownMovements(  /** observable data source */   source = const (1.),
                        /** lag size */                 timeframe = 10.0)

        = Max(0.0, source~>Lagged(timeframe) - source)

    @category = "RSI"
    package {
        /**
         *  Relative Strength Index
         */
        @label = "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)"
        type RSI(/** observable data source */   source      = .const (1.),
                 /** lag size */                 timeframe   = 10.0,
                 /** alpha parameter for EWMA */ alpha       = 0.015)
        {
            /**
             *  Absolute value for Relative Strength Index
             */
            def Raw =
                source~>UpMovements  (timeframe)~>EW(alpha)~>Avg /
                source~>DownMovements(timeframe)~>EW(alpha)~>Avg

            def Value = 100.0 - 100.0 / (1.0 + Raw)
        }

    }

    /**
     *  Log returns
     */
    @label = "LogReturns_{%(timeframe)s}(%(x)s)"
    def LogReturns(/** observable data source */   x = const(1.),
                   /** lag size */                 timeframe   = 10.0)

        =  Log(x / x~>Lagged(timeframe))
}