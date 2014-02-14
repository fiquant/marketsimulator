@category = "Volume function"

package strategy.position() {
    // defined at defs\strategies\parts\position.sc: 4.5
    /** Position function for desired position strategy
     */
    def DesiredPosition(/** observable desired position */ desiredPosition = const(1.0),
                        /** trader in question */ trader = trader.SingleProxy()) = desiredPosition-trader.Position(trader)-trader.PendingVolume(trader)
    
    // defined at defs\strategies\parts\position.sc: 13.5
    /** Position function for Bollinger bands strategy with linear scaling
     */
    def Bollinger_linear(/** alpha parameter for exponentially weighted moving everage and variance */ alpha = 0.15,
                         /** observable scaling function that maps relative deviation to desired position */ k = const(0.5),
                         /** trader in question */ trader = trader.SingleProxy()) = DesiredPosition(observable.OnEveryDt(1.0,math.EW.RelStdDev(orderbook.MidPrice(orderbook.OfTrader(trader)),alpha)*k),trader)
    
    // defined at defs\strategies\parts\position.sc: 32.5
    /** Position function for Relative Strength Index strategy with linear scaling
     */
    def RSI_linear(/** alpha parameter for exponentially moving averages of up movements and down movements */ alpha = 1.0/14.0,
                   /** observable scaling function that maps RSI deviation from 50 to the desired position */ k = const(-0.04),
                   /** lag for calculating up and down movements */ timeframe = 1.0,
                   /** trader in question */ trader = trader.SingleProxy()) = DesiredPosition(observable.OnEveryDt(1.0,(50.0-math.RSI(orderbook.OfTrader(trader),timeframe,alpha))*k),trader)
}
