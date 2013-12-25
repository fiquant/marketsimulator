@category = "Asset's"

package observable.orderbook {
    @python.intrinsic("orderbook.of_trader._OfTrader_Impl")
    @label = "N/A"
    def OfTrader(Trader = trader.SingleProxy()) : IOrderBook
        
    
    @python.intrinsic("orderbook.queue._Queue_Impl")
    @label = "Queue(%(book)s)"
    def Queue(book = OfTrader(),
              side = side.Sell()) : IOrderQueue
        
    
    @python.intrinsic("orderbook.queue._Asks_Impl")
    @label = "Asks(%(book)s)"
    def Asks(book = OfTrader())
         = Queue(book,side.Sell())
    
    @python.intrinsic("orderbook.queue._Bids_Impl")
    @label = "Bids(%(book)s)"
    def Bids(book = OfTrader())
         = Queue(book,side.Buy())
    
    @python.intrinsic("orderbook.props._BestPrice_Impl")
    @label = "Price(%(queue)s)"
    def BestPrice(queue = Asks()) : IObservable[Float]
        
    
    @python()
    @label = "Ask_{%(book)s}"
    def AskPrice(book = OfTrader())
         = BestPrice(Asks(book))
    
    @python()
    @label = "Bid^{%(book)s}"
    def BidPrice(book = OfTrader())
         = BestPrice(Bids(book))
    
    @python.intrinsic("orderbook.last_price._LastPrice_Impl")
    @label = "LastPrice(%(queue)s)"
    def LastPrice(queue = Asks()) : IObservable[Float]
        
    
    @python()
    @label = "Ask_{%(book)s}"
    def AskLastPrice(book = OfTrader())
         = LastPrice(Asks(book))
    
    @python()
    @label = "Bid^{%(book)s}"
    def BidLastPrice(book = OfTrader())
         = LastPrice(Bids(book))
    
    @python.intrinsic("orderbook.last_trade._LastTradePrice_Impl")
    @label = "LastTradePrice(%(queue)s)"
    def LastTradePrice(queue = Asks()) : IObservable[Float]
        
    
    @python()
    @label = "LastTradeAsk_{%(book)s}"
    def AskLastTradePrice(book = OfTrader())
         = LastTradePrice(Asks(book))
    
    @python()
    @label = "LastTradeBid^{%(book)s}"
    def BidLastTradePrice(book = OfTrader())
         = LastTradePrice(Bids(book))
    
    @python.intrinsic("orderbook.last_trade._LastTradeVolume_Impl")
    @label = "LastTradeVolume(%(queue)s)"
    def LastTradeVolume(queue = Asks()) : IObservable[Float]
        
    
    @python.observable()
    @label = "SafeSidePrice^{%(queue)s}"
    def SafeSidePrice(queue = Asks(),
                      defaultValue = constant(100.0))
         = Observable(IfDefined(BestPrice(queue),IfDefined(LastPrice(queue),defaultValue)))
    
    @python()
    @label = "Price_{%(alpha)s}^{%(queue)s}"
    def WeightedPrice(queue = Asks(),
                      alpha = 0.015)
         = EW.Avg(LastTradePrice(queue)*LastTradeVolume(queue),alpha)/EW.Avg(LastTradeVolume(queue),alpha)
    
    @python()
    @label = "Ask_{%(alpha)s}^{%(book)s}"
    def AskWeightedPrice(book = OfTrader(),
                         alpha = 0.015)
         = WeightedPrice(Asks(book),alpha)
    
    @python()
    @label = "Bid_{%(alpha)s}^{%(book)s}"
    def BidWeightedPrice(book = OfTrader(),
                         alpha = 0.015)
         = WeightedPrice(Bids(book),alpha)
    
    @python.intrinsic("orderbook.props._TickSize_Impl")
    @label = "TickSize(%(book)s)"
    def TickSize(book = OfTrader()) : () => Float
        
    
    @python()
    @label = "Spread_{%(book)s}"
    def Spread(book = OfTrader())
         = Observable(AskPrice(book)-BidPrice(book))
    
    @python()
    @label = "MidPrice_{%(book)s}"
    def MidPrice(book = OfTrader())
         = Observable((AskPrice(book)+BidPrice(book))/2.0)
    
    @python.intrinsic("orderbook.cumulative_price.CumulativePrice_Impl")
    @label = "CumulativePrice(%(book)s, %(depth)s)"
    def CumulativePrice(book = OfTrader(),
                        depth = constant()) : IObservable[Float]
        
    
    @python.intrinsic("orderbook.volume_levels.VolumeLevels_Impl")
    @label = "VolumeLevels(%(queue)s)"
    def VolumeLevels(queue = Asks(),
                     volumeDelta = 30.0,
                     volumeCount = 10) : IFunction[VolumeLevels]
        
    
    @python()
    @label = "NaiveCumulativePrice(%(book)s, %(depth)s)"
    def NaiveCumulativePrice(book = OfTrader(),
                             depth = constant())
         = Observable(if depth<0.0 then depth*AskPrice(book) else if depth>0.0 then depth*BidPrice(book) else 0.0)
}
