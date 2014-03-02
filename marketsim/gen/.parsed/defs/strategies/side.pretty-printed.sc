
package strategy() {
    // defined at defs\strategies\side.sc: 3.5
    /** Noise strategy is a quite dummy strategy that randomly chooses trade side and sends market orders
     */
    def Noise(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
              /** order factory function*/ orderFactory = order.side.Market()) = Generic(orderFactory(side.Noise()),eventGen)
    
    // defined at defs\strategies\side.sc: 16.5
    /** Strategy that calculates Relative Strength Index of an asset
     *  and starts to buy when RSI is greater than 50 + *threshold*
     *  and sells when RSI is less than 50 - *thresold*
     */
    def RSIbis(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
               /** order factory function*/ orderFactory = order.side.Market(),
               /** parameter |alpha| for exponentially weighted moving average when calculating RSI */ alpha = 1.0/14,
               /** lag for calculating up and down movements for RSI */ timeframe = 1.0,
               /** strategy starts to act once RSI is out of [50-threshold, 50+threshold] */ threshold = 30.0) = orderFactory(side.Signal(50.0-orderbook.OfTrader()~>RSI(timeframe,alpha),50.0-threshold)~>S_Side)~>Strategy(eventGen)
}
