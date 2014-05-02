@category = "Basic"

package () {
    // defined at defs\graph.sc: 4.5
    /** Observable returning at the end of every *timeframe*
     * open/close/min/max price, its average and standard deviation
     */
    @python.intrinsic("observable.candlestick.CandleSticks_Impl")
    @label = "Candles_{%(source)s}"
    def CandleSticks(/** observable data source considered as asset price */ source = const(1.0),
                     /** size of timeframe */ timeframe = 10.0) : IObservable[ICandleStick]
    
    // defined at defs\graph.sc: 15.5
    /** Time serie to store and render it after on a graph
     *  Used to specify what data should be collected about order books and traders
     */
    @python.intrinsic("timeserie.ToRecord_Impl")
    @label = "%(source)s"
    def TimeSerie(source = const(0.0) : IObservable[Any],
                  graph = veusz.Graph(),
                  _digitsToShow = 4,
                  _smooth = 1) : ITimeSerie
    
    // defined at defs\graph.sc: 26.5
    /** Time serie holding volume levels of an asset
     * Level of volume V is a price at which cumulative volume of better orders is V
     */
    @python.intrinsic("timeserie.VolumeLevels_Impl")
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
    // defined at defs\graph.sc: 45.5
    /** Graph to render at Veusz. Time series are added to it automatically in their constructor
     */
    @python.intrinsic("veusz.Graph_Impl")
    @label = "%(name)s"
    def Graph(name = "graph") : IGraph
    
    // defined at defs\graph.sc: 52.5
    @python.intrinsic("veusz.CSV_Impl")
    def CSV(directory : String,
            source : Any,
            attributes : Any) : Any
    
    // defined at defs\graph.sc: 55.5
    @python.intrinsic("veusz.VolumeLevelProxy_Impl")
    @label = "N/A"
    def VolumeLevelProxy(source : Any,
                         idx : Int) : Any
}
@category = "N/A"

package js() {
    // defined at defs\graph.sc: 63.5
    /** Graph to render at Veusz. Time series are added to it automatically in their constructor
     */
    @python.intrinsic("js.Graph_Impl")
    @label = "%(name)s"
    def Graph(name = "graph") : IGraph
}
