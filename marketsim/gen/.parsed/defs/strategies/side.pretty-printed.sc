
package strategy() {
    // defined at defs\strategies\side.sc: 3.5
    /** Noise strategy is a quite dummy strategy that randomly chooses trade side and sends market orders
     */
    def Noise(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
              /** order factory function*/ orderFactory = order.side.Market()) = Generic(orderFactory(side.Noise()),eventGen)
    
    // defined at defs\strategies\side.sc: 16.5
    /** Signal strategy listens to some discrete signal
     * and when the signal becomes more than some threshold the strategy starts to buy.
     * When the signal gets lower than -threshold the strategy starts to sell.
     */
    def Signal(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
               /** order factory function*/ orderFactory = order.side.Market(),
               /** signal to be listened to */ signal = constant(0.0),
               /** threshold when the trader starts to act */ threshold = 0.7) = orderFactory(side.Signal(signal,threshold))~>Strategy(eventGen)
    
    // defined at defs\strategies\side.sc: 32.5
    /** Trend follower can be considered as a sort of a signal strategy
     * where the *signal* is a trend of the asset.
     * Under trend we understand the first derivative of some moving average of asset prices.
     * If the derivative is positive, the trader buys; if negative - it sells.
     * Since moving average is a continuously changing signal, we check its
     * derivative at moments of time given by *eventGen*.
     */
    def TrendFollower(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                      /** order factory function*/ orderFactory = order.side.Market(),
                      /** parameter |alpha| for exponentially weighted moving average */ ewma_alpha = 0.15,
                      /** threshold when the trader starts to act */ threshold = 0.0) = orderFactory(side.TrendFollower(ewma_alpha,threshold))~>Strategy(eventGen)
    
    // defined at defs\strategies\side.sc: 51.5
    /** Two averages strategy compares two averages of price of the same asset but
     * with different parameters ('slow' and 'fast' averages) and when
     * the first is greater than the second one it buys,
     * when the first is lower than the second one it sells
     */
    def CrossingAverages(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                         /** order factory function*/ orderFactory = order.side.Market(),
                         /** parameter |alpha| for exponentially weighted moving average 1 */ ewma_alpha_1 = 0.15,
                         /** parameter |alpha| for exponentially weighted moving average 2 */ ewma_alpha_2 = 0.015,
                         /** threshold when the trader starts to act */ threshold = 0.0) = orderFactory(side.CrossingAverages(ewma_alpha_1,ewma_alpha_2,threshold))~>Strategy(eventGen)
    
    // defined at defs\strategies\side.sc: 70.5
    /** Strategy that calculates Relative Strength Index of an asset
     *  and starts to buy when RSI is greater than 50 + *threshold*
     *  and sells when RSI is less than 50 - *thresold*
     */
    def RSIbis(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
               /** order factory function*/ orderFactory = order.side.Market(),
               /** parameter |alpha| for exponentially weighted moving average when calculating RSI */ alpha = 1.0/14,
               /** lag for calculating up and down movements for RSI */ timeframe = 1.0,
               /** strategy starts to act once RSI is out of [50-threshold, 50+threshold] */ threshold = 30.0) = orderFactory(side.Signal(50.0-orderbook.OfTrader()~>RSI(timeframe,alpha),50.0-threshold))~>Strategy(eventGen)
}
