@category = "Side function"

package strategy.side() {
    // defined at defs\strategies\parts\side.sc: 4.5
    /** Side function for a noise trading strategy
     */
    def Noise(side_distribution = math.random.uniform(0.0,1.0)) = if side_distribution>0.5 then side.Sell() else side.Buy()
    
    // defined at defs\strategies\parts\side.sc: 11.5
    /** Side function for signal strategy
     */
    @python.observable()
    def Signal(/** signal to be listened to */ signal = constant(0.0),
               /** threshold when the trader starts to act */ threshold = 0.7) = if signal>threshold then side.Buy() else if signal<0-threshold then side.Sell() else side.Nothing()
    
    // defined at defs\strategies\parts\side.sc: 24.5
    /** Side function for trend follower strategy
     */
    def TrendFollower(/** parameter |alpha| for exponentially weighted moving average */ alpha = 0.15,
                      /** threshold when the trader starts to act */ threshold = 0.0,
                      /** asset in question */ book = orderbook.OfTrader()) = Signal(book~>MidPrice~>EW(alpha)~>Avg~>Derivative,threshold)
    
    // defined at defs\strategies\parts\side.sc: 37.5
    /** Side function for crossing averages strategy
     */
    def CrossingAverages(/** parameter |alpha| for exponentially weighted moving average 1 */ alpha_1 = 0.15,
                         /** parameter |alpha| for exponentially weighted moving average 2 */ alpha_2 = 0.015,
                         /** threshold when the trader starts to act */ threshold = 0.0,
                         /** asset in question */ book = orderbook.OfTrader()) = Signal(book~>MidPrice~>EW(alpha_1)~>Avg-book~>MidPrice~>EW(alpha_2)~>Avg,threshold)
    
    // defined at defs\strategies\parts\side.sc: 55.5
    /** Side function for fundamental value strategy
     */
    def FundamentalValue(/** observable fundamental value */ fv = constant(200.0),
                         /** asset in question */ book = orderbook.OfTrader()) = if book~>Bids~>BestPrice>fv then side.Sell() else if book~>Asks~>BestPrice<fv then side.Buy() else side.Nothing()
    
    // defined at defs\strategies\parts\side.sc: 68.5
    /** Side function for mean reversion strategy
     */
    def MeanReversion(/** parameter |alpha| for exponentially weighted moving average */ alpha = 0.015,
                      /** asset in question */ book = orderbook.OfTrader()) = FundamentalValue(book~>MidPrice~>EW(alpha)~>Avg,book)
    
    // defined at defs\strategies\parts\side.sc: 81.5
    /** Side function for pair trading strategy
     */
    def PairTrading(/** reference to order book for another asset used to evaluate fair price of our asset */ bookToDependOn = orderbook.OfTrader(),
                    /** multiplier to obtain fair asset price from the reference asset price */ factor = 1.0,
                    /** asset in question */ book = orderbook.OfTrader()) = FundamentalValue(bookToDependOn~>MidPrice*factor,book)
}
