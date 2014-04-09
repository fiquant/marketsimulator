@category = "Side function"

package strategy.side() {
    abstract type SideStrategy
    {
        // defined at defs\strategies\side.sc: 6.9
        def Strategy(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                     /** order factory function*/ orderFactory = order.side.Market()) = Generic(orderFactory(Side),eventGen)
    }
    
    type Noise(side_distribution = math.random.uniform(0.0,1.0)) : SideStrategy
    {
        // defined at defs\strategies\side.sc: 16.9
        def Side() = if side_distribution>0.5 then side.Buy() else side.Sell()
    }
    
    abstract type SignalStrategy() : SideStrategy
    {
        // defined at defs\strategies\side.sc: 21.9
        def Side() = if Signal_Value>threshold then side.Buy() else if Signal_Value<0-threshold then side.Sell() else side.Nothing()
    }
    
    type Signal(/** signal to be listened to */ source = .constant(0.0),/** threshold when the trader starts to act */ threshold = 0.7) : SignalStrategy
    {
        // defined at defs\strategies\side.sc: 37.9
        def Signal_Value() = source
    }
    
    type TrendFollower(/** parameter |alpha| for exponentially weighted moving average */ alpha = 0.15,/** threshold when the trader starts to act */ threshold = 0.0,/** asset in question */ book = .orderbook.OfTrader()) : SignalStrategy
    {
        // defined at defs\strategies\side.sc: 58.9
        def Signal_Value() = book~>MidPrice~>EW(alpha)~>Avg~>Derivative
    }
    
    type CrossingAverages(/** parameter |alpha| for exponentially weighted moving average 1 */ alpha_1 = 0.15,/** parameter |alpha| for exponentially weighted moving average 2 */ alpha_2 = 0.015,/** threshold when the trader starts to act */ threshold = 0.0,/** asset in question */ book = .orderbook.OfTrader()) : SignalStrategy
    {
        // defined at defs\strategies\side.sc: 81.9
        def Signal_Value() = book~>MidPrice~>EW(alpha_1)~>Avg-book~>MidPrice~>EW(alpha_2)~>Avg
    }
    
    abstract type FundamentalValueStrategy() : SideStrategy
    {
        // defined at defs\strategies\side.sc: 87.9
        def book() = .orderbook.OfTrader()
        
        // defined at defs\strategies\side.sc: 89.9
        def Side() = if book~>Bids~>BestPrice>Fundamental_Value then side.Sell() else if book~>Asks~>BestPrice<Fundamental_Value then side.Buy() else side.Nothing()
    }
    
    type FundamentalValue(/** observable fundamental value */ fv = .constant(200.0)) : FundamentalValueStrategy
    {
        // defined at defs\strategies\side.sc: 104.9
        def Fundamental_Value() = fv
    }
    
    type MeanReversion(/** parameter |alpha| for exponentially weighted moving average */ alpha = 0.15) : FundamentalValueStrategy
    {
        // defined at defs\strategies\side.sc: 117.9
        def Fundamental_Value() = book~>MidPrice~>EW(alpha)~>Avg
    }
    
    type PairTrading(/** reference to order book for another asset
      * used to evaluate fair price of our asset */ bookToDependOn = .orderbook.OfTrader(),/** multiplier to obtain fair asset price from the reference asset price */ factor = 1.0) : FundamentalValueStrategy
    {
        // defined at defs\strategies\side.sc: 135.9
        def Fundamental_Value() = bookToDependOn~>MidPrice*factor
    }
    
    type RSIbis(/** parameter |alpha| for exponentially weighted moving average when calculating RSI */ alpha = 1.0/14,/** lag for calculating up and down movements for RSI */ timeframe = 1.0,/** strategy starts to act once RSI is out of [50-threshold, 50+threshold] */ threshold = 30.0) : SignalStrategy
    {
        // defined at defs\strategies\side.sc: 145.9
        def Signal_Value() = 50.0-orderbook.OfTrader()~>MidPrice~>RSI(timeframe,alpha)~>Value
    }
}
