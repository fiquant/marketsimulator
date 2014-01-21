@category = "Basic"

package () {
    @python.intrinsic("observable.candlestick.CandleSticks_Impl")
    @label = "Candles_{%(source)s}"
    def CandleSticks(source = const(),
                     timeframe = 10.0) : IObservable[CandleStick]
        
    
    @python.intrinsic("timeserie._ToRecord_Impl")
    @label = "%(source)s"
    def TimeSerie(source = const(0.0) : IObservable[Any],
                  graph = veusz.Graph(),
                  _digitsToShow = 4,
                  _smooth = 1) : ITimeSerie
        
    
    @python.intrinsic("timeserie._VolumeLevels_Impl")
    @label = "%(source)s"
    def volumeLevels(source : IFunction[IVolumeLevels],
                     graph = veusz.Graph(),
                     _digitsToShow = 4,
                     _smooth = 1,
                     _volumes = [30.0],
                     _isBuy = 1) : ITimeSerie
        
}
@category = "N/A"

package veusz() {
    @python.intrinsic("veusz._Graph_Impl")
    def Graph(name = "graph") : IGraph
        
}
