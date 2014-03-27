@category = "Basic"
package
{
    /**
     * Observable returning at the end of every *timeframe*
     * open/close/min/max price, its average and standard deviation
     */
    @python.intrinsic("observable.candlestick.CandleSticks_Impl")
    @label = "Candles_{%(source)s}"
    def CandleSticks(/** observable data source considered as asset price */
                     source     = const(1.),
                     /** size of timeframe */
                     timeframe  = 10.0) : IObservable[ICandleStick]

    /**
     *  Time serie to store and render it after on a graph
     *  Used to specify what data should be collected about order books and traders
     */
    @python.intrinsic("timeserie.ToRecord_Impl")
    @label = "%(source)s"
    def TimeSerie(source        = const(0.) : IObservable[Any],
                  graph         = veusz.Graph(),
                  _digitsToShow = 4,
                  _smooth       = 1) : ITimeSerie

    /**
     * Time serie holding volume levels of an asset
     * Level of volume V is a price at which cumulative volume of better orders is V
     */
    @python.intrinsic("timeserie.VolumeLevels_Impl")
    @label = "%(source)s"
    def volumeLevels(source        : IFunction[IVolumeLevels],
                     graph         = veusz.Graph(),
                     _digitsToShow = 4,
                     _smooth       = 1,
                     _volumes      = [30.],
                     _isBuy        = 1)
        : ITimeSerie
}


@category = "N/A"
package veusz
{
    /**
     *  Graph to render at Veusz. Time series are added to it automatically in their constructor
     */
    @python.intrinsic("veusz.Graph_Impl")
    def Graph(name = "graph") : IGraph
}
