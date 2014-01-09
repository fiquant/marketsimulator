@category = "Asset's"

package observable.orderbook {
    @python.intrinsic("orderbook.of_trader._OfTrader_Impl")
    @label = "N/A"
    def OfTrader(Trader = trader.SingleProxy()) : IOrderBook
        
    
    @python.intrinsic("orderbook.queue._Queue_Impl")
    def Queue(book = OfTrader(),
              side = side.Sell()) : IOrderQueue
        
    
    @python.intrinsic("orderbook.queue._Asks_Impl")
    def Asks(book = OfTrader())
         = Queue(book,side.Sell())
    
    @python.intrinsic("orderbook.queue._Bids_Impl")
    def Bids(book = OfTrader())
         = Queue(book,side.Buy())
    
    @python.intrinsic("orderbook.props._BestPrice_Impl")
    def BestPrice(queue = Asks()) : IObservable[Price]
        
    
    @label = "Ask_{%(book)s}"
    def AskPrice(book = OfTrader())
         = BestPrice(Asks(book))
    
    @label = "Bid^{%(book)s}"
    def BidPrice(book = OfTrader())
         = BestPrice(Bids(book))
    
    @python.intrinsic("orderbook.last_price._LastPrice_Impl")
    def LastPrice(queue = Asks()) : IObservable[Price]
        
    
    @label = "LastAsk_{%(book)s}"
    def AskLastPrice(book = OfTrader())
         = LastPrice(Asks(book))
    
    @label = "LastBid^{%(book)s}"
    def BidLastPrice(book = OfTrader())
         = LastPrice(Bids(book))
    
    @python.intrinsic("orderbook.last_trade._LastTradePrice_Impl")
    def LastTradePrice(queue = Asks()) : IObservable[Price]
        
    
    def AskLastTradePrice(book = OfTrader())
         = LastTradePrice(Asks(book))
    
    def BidLastTradePrice(book = OfTrader())
         = LastTradePrice(Bids(book))
    
    @python.intrinsic("orderbook.last_trade._LastTradeVolume_Impl")
    def LastTradeVolume(queue = Asks()) : IObservable[Volume]
        
    
    @python.observable()
    def SafeSidePrice(queue = Asks(),
                      defaultValue = constant(100.0))
         = ObservablePrice(IfDefined(BestPrice(queue),IfDefined(LastPrice(queue),defaultValue)))
    
    @label = "Price_{%(alpha)s}^{%(queue)s}"
    def WeightedPrice(queue = Asks(),
                      alpha = 0.015)
         = EW.Avg(LastTradePrice(queue)*LastTradeVolume(queue),alpha)/EW.Avg(LastTradeVolume(queue),alpha)
    
    @label = "Ask_{%(alpha)s}^{%(book)s}"
    def AskWeightedPrice(book = OfTrader(),
                         alpha = 0.015)
         = WeightedPrice(Asks(book),alpha)
    
    @label = "Bid_{%(alpha)s}^{%(book)s}"
    def BidWeightedPrice(book = OfTrader(),
                         alpha = 0.015)
         = WeightedPrice(Bids(book),alpha)
    
    @python.intrinsic("orderbook.props._TickSize_Impl")
    def TickSize(book = OfTrader()) : () => Price
        
    
    def Spread(book = OfTrader())
         = ObservablePrice(AskPrice(book)-BidPrice(book))
    
    def MidPrice(book = OfTrader())
         = ObservablePrice((AskPrice(book)+BidPrice(book))/2.0)
    
    @python.intrinsic("orderbook.cumulative_price.CumulativePrice_Impl")
    def CumulativePrice(book = OfTrader(),
                        depth = constant()) : IObservable[Price]
        
    
    @python.intrinsic("orderbook.volume_levels.VolumeLevels_Impl")
    @label = "VolumeLevels(%(queue)s)"
    def VolumeLevels(queue = Asks(),
                     volumeDelta = 30.0,
                     volumeCount = 10) : IFunction[VolumeLevels]
        
    
    def NaiveCumulativePrice(book = OfTrader(),
                             depth = constant())
         = ObservablePrice(if depth<0.0 then depth*AskPrice(book) else if depth>0.0 then depth*BidPrice(book) else 0.0)
}
