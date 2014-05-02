@category = "Asset"

package orderbook() {
    // defined at defs\orderbook\properties.sc: 4.5
    /** Returns order queue of order *book* for trade *side*
     */
    @python.intrinsic("orderbook.proxy.Queue_Impl")
    def Queue(book = OfTrader(),
              side = side.Sell()) : IOrderQueue
    
    // defined at defs\orderbook\properties.sc: 10.5
    /** Returns sell side order queue for *book*
     */
    @python.intrinsic("orderbook.proxy.Asks_Impl")
    def Asks(book = OfTrader()) = Queue(book,side.Sell())
    
    // defined at defs\orderbook\properties.sc: 16.5
    /** Returns buy side order queue for *book*
     */
    @python.intrinsic("orderbook.proxy.Bids_Impl")
    def Bids(book = OfTrader()) = Queue(book,side.Buy())
    
    // defined at defs\orderbook\properties.sc: 22.5
    /** Returns best order price of *queue*
     *  Returns None is *queue* is empty
     */
    @python.intrinsic("orderbook.props.BestPrice_Impl")
    def BestPrice(queue = Asks()) : IObservable[Price]
    
    // defined at defs\orderbook\properties.sc: 29.5
    /** Returns last defined price at *queue*
     *  Returns None is *queue* has been always empty
     */
    @python.intrinsic("orderbook.last_price.LastPrice_Impl")
    def LastPrice(queue = Asks()) : IObservable[Price]
    
    // defined at defs\orderbook\properties.sc: 36.5
    /** Returns price of the last trade at *queue*
     *  Returns None if there haven't been any trades
     */
    @python.intrinsic("orderbook.last_trade.LastTradePrice_Impl")
    def LastTradePrice(queue = Asks()) : IObservable[Price]
    
    // defined at defs\orderbook\properties.sc: 43.5
    /** Returns volume of the last trade at *queue*
     *  Returns None if there haven't been any trades
     */
    @python.intrinsic("orderbook.last_trade.LastTradeVolume_Impl")
    def LastTradeVolume(queue = Asks()) : IObservable[Volume]
    
    // defined at defs\orderbook\properties.sc: 50.5
    /** Returns best price if defined, otherwise last price
     *  and *defaultValue* if there haven't been any trades
     */
    @python.observable()
    def SafeSidePrice(queue = Asks(),
                      /** price to be used if there haven't been any trades */ defaultValue = constant(100.0)) = queue~>BestPrice~>getOrElse(queue~>LastPrice~>getOrElse(defaultValue))
    
    // defined at defs\orderbook\properties.sc: 63.5
    /** Returns moving average of trade prices weighted by their volumes
     */
    @label = "Price_{%(alpha)s}^{%(queue)s}"
    def WeightedPrice(queue = Asks(),
                      /** parameter alpha for the moving average  */ alpha = 0.15) = queue~>LastTradePrice*queue~>LastTradeVolume~>EW(alpha)~>Avg/queue~>LastTradeVolume~>EW(alpha)~>Avg
    
    // defined at defs\orderbook\properties.sc: 74.5
    /** Returns tick size for the order *book*
     */
    @python.intrinsic("orderbook.props.TickSize_Impl")
    def TickSize(book = OfTrader()) : () => Price
    
    // defined at defs\orderbook\properties.sc: 80.5
    /** Spread of order *book*
     */
    def Spread(book = OfTrader()) = book~>Asks~>BestPrice-book~>Bids~>BestPrice
    
    // defined at defs\orderbook\properties.sc: 86.5
    /** MidPrice of order *book*
     */
    def MidPrice(book = OfTrader()) = (book~>Asks~>BestPrice+book~>Bids~>BestPrice)/2.0
    
    // defined at defs\orderbook\properties.sc: 92.5
    /** Returns price for best orders of total volume *depth*
     *
     *  In other words cumulative price corresponds to trader balance change
     *  if a market order of volume *depth* is completely matched
     *
     *  Negative *depth* correponds to will buy assets
     *  Positive *depth* correponds to will sell assets
     */
    @python.intrinsic("orderbook.cumulative_price.CumulativePrice_Impl")
    def CumulativePrice(book = OfTrader(),
                        depth = constant(1.0)) : IObservable[Price]
    
    // defined at defs\orderbook\properties.sc: 105.5
    /** Returns naive approximation of price for best orders of total volume *depth*
     *  by taking into account prices only for the best order
     *
     *  Negative *depth* correponds to will buy assets
     *  Positive *depth* correponds to will sell assets
     */
    def NaiveCumulativePrice(book = OfTrader(),
                             depth = constant(1.0)) = if depth<0.0 then depth*book~>Asks~>BestPrice else if depth>0.0 then depth*book~>Bids~>BestPrice else 0.0
    
    // defined at defs\orderbook\properties.sc: 119.5
    /** Returns arrays of levels for given volumes [i*volumeDelta for i in range(0, volumeCount)]
     *  Level of volume V is a price at which cumulative volume of better orders is V
     */
    @python.intrinsic("orderbook.volume_levels.VolumeLevels_Impl")
    @label = "VolumeLevels(%(queue)s)"
    def VolumeLevels(queue = Asks(),
                     /** distance between two volumes */ volumeDelta = 30.0,
                     /** number of volume levels to track */ volumeCount = 10) : IObservable[IVolumeLevels]
}
