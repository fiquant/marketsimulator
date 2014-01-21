@category = "Side function"

package observable.sidefunc() {
    def Noise(side_distribution = math.random.uniform(0.0,1.0) : IFunction[Float])
         = if side_distribution>0.5 then side.Sell() else side.Buy()
    
    @python.observable()
    def Signal(signal = constant(),
               threshold = 0.7)
         = if signal>threshold then side.Buy() else if signal<0-threshold then side.Sell() else side.Nothing()
    
    def TrendFollower(alpha = 0.015,
                      threshold = 0.0,
                      book = orderbook.OfTrader())
         = Signal(math.Derivative(math.EW.Avg(orderbook.MidPrice(book),alpha)),threshold)
    
    def CrossingAverages(alpha_1 = 0.015,
                         alpha_2 = 0.15,
                         threshold = 0.0,
                         book = orderbook.OfTrader())
         = Signal(math.EW.Avg(orderbook.MidPrice(book),alpha_1)-math.EW.Avg(orderbook.MidPrice(book),alpha_2),threshold)
    
    @python.observable()
    def FundamentalValue(fv = constant(200.0),
                         book = orderbook.OfTrader())
         = if orderbook.bid.Price(book)>fv then side.Sell() else if orderbook.ask.Price(book)<fv then side.Buy() else side.Nothing()
    
    def MeanReversion(alpha = 0.015,
                      book = orderbook.OfTrader())
         = FundamentalValue(math.EW.Avg(orderbook.MidPrice(book),alpha),book)
    
    def PairTrading(dependee = orderbook.OfTrader(),
                    factor = 1.0,
                    book = orderbook.OfTrader())
         = ObservableSide(FundamentalValue(orderbook.MidPrice(dependee)*factor,book))
}
