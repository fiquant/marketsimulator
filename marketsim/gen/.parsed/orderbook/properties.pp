@category = "Asset"

package orderbook() {
    @python.intrinsic("orderbook.proxy._Queue_Impl")
    def Queue(book = OfTrader(),
              side = side.Sell()) : IOrderQueue
        
    
    @python.intrinsic("orderbook.proxy._Asks_Impl")
    def Asks(book = OfTrader())
         = Queue(book,side.Sell())
    
    @python.intrinsic("orderbook.proxy._Bids_Impl")
    def Bids(book = OfTrader())
         = Queue(book,side.Buy())
    
    @python.intrinsic("orderbook.props._BestPrice_Impl")
    def BestPrice(queue = Asks()) : IObservable[Price]
        
    
    @python.intrinsic("orderbook.last_price._LastPrice_Impl")
    def LastPrice(queue = Asks()) : IObservable[Price]
        
    
    @python.intrinsic("orderbook.last_trade._LastTradePrice_Impl")
    def LastTradePrice(queue = Asks()) : IObservable[Price]
        
    
    @python.intrinsic("orderbook.last_trade._LastTradeVolume_Impl")
    def LastTradeVolume(queue = Asks()) : IObservable[Volume]
        
    
    @python.observable()
    def SafeSidePrice(queue = Asks(),
                      defaultValue = constant(100.0))
         = observable.Price(IfDefined(BestPrice(queue),IfDefined(LastPrice(queue),defaultValue)))
    
    @label = "Price_{%(alpha)s}^{%(queue)s}"
    def WeightedPrice(queue = Asks(),
                      alpha = 0.15)
         = math.EW.Avg(LastTradePrice(queue)*LastTradeVolume(queue),alpha)/math.EW.Avg(LastTradeVolume(queue),alpha)
    
    @python.intrinsic("orderbook.props._TickSize_Impl")
    def TickSize(book = OfTrader()) : () => Price
        
    
    def Spread(book = OfTrader())
         = observable.Price(ask.Price(book)-bid.Price(book))
    
    def MidPrice(book = OfTrader())
         = observable.Price((ask.Price(book)+bid.Price(book))/2.0)
    
    @python.intrinsic("orderbook.cumulative_price.CumulativePrice_Impl")
    def CumulativePrice(book = OfTrader(),
                        depth = constant()) : IObservable[Price]
        
    
    @python.intrinsic("orderbook.volume_levels.VolumeLevels_Impl")
    @label = "VolumeLevels(%(queue)s)"
    def VolumeLevels(queue = Asks(),
                     volumeDelta = 30.0,
                     volumeCount = 10) : IObservable[IVolumeLevels]
        
    
    def NaiveCumulativePrice(book = OfTrader(),
                             depth = constant())
         = observable.Price(if depth<0.0 then depth*ask.Price(book) else if depth>0.0 then depth*bid.Price(book) else 0.0)
    
    abstract package _base_impl() {
        @label = "{{queue}}"
        def Price(book = OfTrader())
             = BestPrice(_queue(book))
        
        @label = "Last({{queue}})"
        def LastPrice(book = OfTrader())
             = orderbook.LastPrice(_queue(book))
        
        @label = "LastTrade({{queue}})"
        def LastTradePrice(book = OfTrader())
             = orderbook.LastTradePrice(_queue(book))
        
        @label = "LastTradeVolume({{queue}})"
        def LastTradeVolume(book = OfTrader())
             = orderbook.LastTradeVolume(_queue(book))
        
        @label = "[{{queue}}]_{%(alpha)s}"
        def WeightedPrice(book = OfTrader(),
                          alpha = 0.15)
             = orderbook.WeightedPrice(_queue(book),alpha)
    }
    @queue = "Ask_{%(book)s}"
    
    package ask() extends _base_impl {
        def _queue = Asks
    }
    @queue = "Bid^{%(book)s}"
    
    package bid() extends _base_impl {
        def _queue = Bids
    }
}
