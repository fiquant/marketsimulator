@category = "Volume function"

package strategy.position() {
    abstract type DesiredPositionStrategy
    {
        // defined at defs\strategies\position.sc: 6.9
        def Position() = DesiredPosition-trader~>Position-trader~>PendingVolume
        
        // defined at defs\strategies\position.sc: 8.9
        def Strategy(/** order factory function */ orderFactory = order.signedVolume.MarketSigned()) = orderFactory(Position)~>Strategy
    }
    
    type Bollinger_linear(/** alpha parameter for exponentially weighted
      * moving everage and variance */ alpha = 0.15,/** observable scaling function that maps
      * relative deviation to desired position */ k = .const(0.5),/** trader in question */ trader = .trader.SingleProxy()) : DesiredPositionStrategy
    {
        // defined at defs\strategies\position.sc: 26.9
        def DesiredPosition() = trader~>Orderbook~>MidPrice~>EW(alpha)~>RelStdDev~>OnEveryDt(1.0)*k
    }
    
    type RSI_linear(/** alpha parameter for exponentially moving averages of up movements and down movements */ alpha = 1.0/14.0,/** observable scaling function that maps RSI deviation from 50 to the desired position */ k = .const(-0.04),/** lag for calculating up and down movements */ timeframe = 1.0,/** trader in question */ trader = .trader.SingleProxy()) : DesiredPositionStrategy
    {
        // defined at defs\strategies\position.sc: 44.9
        def DesiredPosition() = (50.0-trader~>Orderbook~>MidPrice~>RSI(timeframe,alpha)~>Value~>OnEveryDt(1.0))*k
    }
}
