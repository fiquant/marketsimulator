@category = "Asset"

package orderbook {
    // defined at defs\orderbook\properties.sc: 4.5
    /** Returns order queue of order *book* for trade *side*
     */
    @python.intrinsic("orderbook.proxy._Queue_Impl")
    def Queue(book = OfTrader(),
              side = side.Sell()) : IOrderQueue
    
    // defined at defs\orderbook\properties.sc: 10.5
    /** Returns sell side order queue for *book*
     */
    @python.intrinsic("orderbook.proxy._Asks_Impl")
    def Asks(book = OfTrader()) = Queue(book,side.Sell())
    
    // defined at defs\orderbook\properties.sc: 16.5
    /** Returns buy side order queue for *book*
     */
    @python.intrinsic("orderbook.proxy._Bids_Impl")
    def Bids(book = OfTrader()) = Queue(book,side.Buy())
    
    // defined at defs\orderbook\properties.sc: 22.5
    /** Returns best order price of *queue*
     *  Returns None is *queue* is empty
     */
    @python.intrinsic("orderbook.props._BestPrice_Impl")
    def BestPrice(queue = Asks()) : IObservable[Price]
    
    // defined at defs\orderbook\properties.sc: 29.5
    /** Returns last defined price at *queue*
     *  Returns None is *queue* has been always empty
     */
    @python.intrinsic("orderbook.last_price._LastPrice_Impl")
    def LastPrice(queue = Asks()) : IObservable[Price]
    
    // defined at defs\orderbook\properties.sc: 36.5
    /** Returns price of the last trade at *queue*
     *  Returns None if there haven't been any trades
     */
    @python.intrinsic("orderbook.last_trade._LastTradePrice_Impl")
    def LastTradePrice(queue = Asks()) : IObservable[Price]
    
    // defined at defs\orderbook\properties.sc: 43.5
    /** Returns volume of the last trade at *queue*
     *  Returns None if there haven't been any trades
     */
    @python.intrinsic("orderbook.last_trade._LastTradeVolume_Impl")
    def LastTradeVolume(queue = Asks()) : IObservable[Volume]
    
    // defined at defs\orderbook\properties.sc: 50.5
    /** Returns best price if defined, otherwise last price
     *  and *defaultValue* if there haven't been any trades
     */
    @python.observable()
    def SafeSidePrice(queue = Asks(),
                      /** price to be used if there haven't been any trades */ defaultValue = constant(100.0)) = observable.Price(IfDefined(BestPrice(queue),IfDefined(LastPrice(queue),defaultValue)))
    
    // defined at defs\orderbook\properties.sc: 63.5
    /** Returns moving average of trade prices weighted by their volumes
     */
    @label = "Price_{%(alpha)s}^{%(queue)s}"
    def WeightedPrice(queue = Asks(),
                      /** parameter alpha for the moving average  */ alpha = 0.15) = math.EW.Avg(LastTradePrice(queue)*LastTradeVolume(queue),alpha)/math.EW.Avg(LastTradeVolume(queue),alpha)
    
    // defined at defs\orderbook\properties.sc: 74.5
    /** Returns tick size for the order *book*
     */
    @python.intrinsic("orderbook.props._TickSize_Impl")
    def TickSize(book = OfTrader()) : () => Price
    
    // defined at defs\orderbook\properties.sc: 80.5
    /** Spread of order *book*
     */
    def Spread(book = OfTrader()) = observable.Price(ask.Price(book)-bid.Price(book))
    
    // defined at defs\orderbook\properties.sc: 88.5
    /** MidPrice of order *book*
     */
    def MidPrice(book = OfTrader()) = observable.Price((ask.Price(book)+bid.Price(book))/2.0)
    
    // defined at defs\orderbook\properties.sc: 96.5
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
                        depth = constant()) : IObservable[Price]
    
    // defined at defs\orderbook\properties.sc: 109.5
    /** Returns naive approximation of price for best orders of total volume *depth*
     *  by taking into account prices only for the best order
     *
     *  Negative *depth* correponds to will buy assets
     *  Positive *depth* correponds to will sell assets
     */
    def NaiveCumulativePrice(book = OfTrader(),
                             depth = constant()) = observable.Price(if depth<0.0 then depth*ask.Price(book) else if depth>0.0 then depth*bid.Price(book) else 0.0)
    
    // defined at defs\orderbook\properties.sc: 124.5
    /** Returns arrays of levels for given volumes [i*volumeDelta for i in range(0, volumeCount)]
     *  Level of volume V is a price at which cumulative volume of better orders is V
     */
    @python.intrinsic("orderbook.volume_levels.VolumeLevels_Impl")
    @label = "VolumeLevels(%(queue)s)"
    def VolumeLevels(queue = Asks(),
                     /** distance between two volumes */ volumeDelta = 30.0,
                     /** number of volume levels to track */ volumeCount = 10) : IObservable[IVolumeLevels]
    
    abstract package _base_impl {
        // defined at defs\orderbook\properties.sc: 140.9
        @label = "{{queue}}"
        def Price(book = OfTrader()) = BestPrice(_queue(book))
        
        // defined at defs\orderbook\properties.sc: 143.9
        @label = "Last({{queue}})"
        def LastPrice(book = OfTrader()) = orderbook.LastPrice(_queue(book))
        
        // defined at defs\orderbook\properties.sc: 146.9
        @label = "LastTrade({{queue}})"
        def LastTradePrice(book = OfTrader()) = orderbook.LastTradePrice(_queue(book))
        
        // defined at defs\orderbook\properties.sc: 149.9
        @label = "LastTradeVolume({{queue}})"
        def LastTradeVolume(book = OfTrader()) = orderbook.LastTradeVolume(_queue(book))
        
        // defined at defs\orderbook\properties.sc: 152.9
        @label = "[{{queue}}]_{%(alpha)s}"
        def WeightedPrice(book = OfTrader(),
                          alpha = 0.15) = orderbook.WeightedPrice(_queue(book),alpha)
    }
    @queue = "Ask_{%(book)s}"
    
    package ask extends _base_impl {
        def _queue = Asks
    }
    @queue = "Bid^{%(book)s}"
    
    package bid extends _base_impl {
        def _queue = Bids
    }
}
