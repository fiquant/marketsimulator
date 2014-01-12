
package strategy {
    /** Noise strategy is a quite dummy strategy that randomly creates an order and sends it to the order book.
     */
    def Noise(/** Event source making the strategy to wake up*/ eventGen = event.Every(mathutils.rnd.expovariate(1.0)),
              /** order factory function*/ orderFactory = order._.side.Market())
         = Generic(orderFactory(observable.sidefunc.Noise()),eventGen)
    
    /** Signal strategy listens to some discrete signal
     * and when the signal becomes more than some threshold the strategy starts to buy.
     * When the signal gets lower than -threshold the strategy starts to sell.
     */
    def Signal(/** Event source making the strategy to wake up*/ eventGen = event.Every(mathutils.rnd.expovariate(1.0)),
               /** order factory function*/ orderFactory = order._.side.Market(),
               /** signal to be listened to */ signal = constant(0.0),
               /** threshold when the trader starts to act */ threshold = 0.7)
         = Generic(orderFactory(observable.sidefunc.Signal(signal,threshold)),eventGen)
    
    /** Trend follower can be considered as a sort of a signal strategy
     * where the *signal* is a trend of the asset.
     * Under trend we understand the first derivative of some moving average of asset prices.
     * If the derivative is positive, the trader buys; if negative - it sells.
     * Since moving average is a continuously changing signal, we check its
     * derivative at moments of time given by *eventGen*.
     */
    def TrendFollower(/** Event source making the strategy to wake up*/ eventGen = event.Every(mathutils.rnd.expovariate(1.0)),
                      /** order factory function*/ orderFactory = order._.side.Market(),
                      /** parameter |alpha| for exponentially weighted moving average */ ewma_alpha = 0.15,
                      /** threshold when the trader starts to act */ threshold = 0.0)
         = Generic(orderFactory(observable.sidefunc.TrendFollower(ewma_alpha,threshold)),eventGen)
    
    /** Two averages strategy compares two averages of price of the same asset but
     * with different parameters ('slow' and 'fast' averages) and when
     * the first is greater than the second one it buys,
     * when the first is lower than the second one it sells
     */
    def CrossingAverages(/** Event source making the strategy to wake up*/ eventGen = event.Every(mathutils.rnd.expovariate(1.0)),
                         /** order factory function*/ orderFactory = order._.side.Market(),
                         /** parameter |alpha| for exponentially weighted moving average 1 */ ewma_alpha_1 = 0.15,
                         /** parameter |alpha| for exponentially weighted moving average 2 */ ewma_alpha_2 = 0.015,
                         /** threshold when the trader starts to act */ threshold = 0.0)
         = Generic(orderFactory(observable.sidefunc.CrossingAverages(ewma_alpha_1,ewma_alpha_2,threshold)),eventGen)
    
    /** Fundamental value strategy believes that an asset should have some specific price
     * (*fundamental value*) and if the current asset price is lower than the fundamental value
     * it starts to buy the asset and if the price is higher it starts to sell the asset.
     */
    def FundamentalValue(/** Event source making the strategy to wake up*/ eventGen = event.Every(mathutils.rnd.expovariate(1.0)),
                         /** order factory function*/ orderFactory = order._.side.Market(),
                         /** defines fundamental value */ fundamentalValue = constant(100.0))
         = Generic(orderFactory(observable.sidefunc.FundamentalValue(fundamentalValue)),eventGen)
    
    /** Mean reversion strategy believes that asset price should return to its average value.
     * It estimates this average using some functional and
     * if the current asset price is lower than the average
     * it buys the asset and if the price is higher it sells the asset.
     */
    def MeanReversion(/** Event source making the strategy to wake up*/ eventGen = event.Every(mathutils.rnd.expovariate(1.0)),
                      /** order factory function*/ orderFactory = order._.side.Market(),
                      /** parameter |alpha| for exponentially weighted moving average */ ewma_alpha = 0.15)
         = Generic(orderFactory(observable.sidefunc.MeanReversion(ewma_alpha)),eventGen)
    
    /** Dependent price strategy believes that the fair price of an asset *A*
     * is completely correlated with price of another asset *B* and the following relation
     * should be held: *PriceA* = *kPriceB*, where *k* is some factor.
     * It may be considered as a variety of a fundamental value strategy
     * with the exception that it is invoked every the time price of another
     * asset *B* changes.
     */
    def PairTrading(/** Event source making the strategy to wake up*/ eventGen = event.Every(mathutils.rnd.expovariate(1.0)),
                    /** order factory function*/ orderFactory = order._.side.Market(),
                    /** reference to order book for another asset used to evaluate fair price of our asset */ bookToDependOn = observable.orderbook.OfTrader(),
                    /** multiplier to obtain fair asset price from the reference asset price */ factor = 1.0)
         = Generic(orderFactory(observable.sidefunc.PairTrading(bookToDependOn,factor)),eventGen)
    
    def RSIbis(/** Event source making the strategy to wake up*/ eventGen = event.Every(mathutils.rnd.expovariate(1.0)),
               /** order factory function*/ orderFactory = order._.side.Market(),
               /** parameter |alpha| for exponentially weighted moving average */ alpha = 1.0/14,
               timeframe = 1.0,
               threshold = 30.0)
         = Generic(orderFactory(observable.sidefunc.Signal(50.0-observable.RSI(observable.orderbook.OfTrader(),timeframe,alpha),50.0-threshold)),eventGen)
}
