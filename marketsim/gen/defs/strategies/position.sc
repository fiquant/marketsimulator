@category = "Volume function"
package strategy.position
{
    abstract type DesiredPositionStrategy
    {
        def Position = DesiredPosition - trader~>Position - trader~>PendingVolume

        def Strategy(/** order factory function */
                    orderFactory = order.signedVolume.MarketSigned()) = (orderFactory(Position))~>Strategy
    }

    /**
     *  Strategy believing that trader position should be proportional to the relative standard deviation of its price
     */
    type Bollinger_linear(
                /** alpha parameter for exponentially weighted moving everage and variance */
                alpha   = 0.15,
                /** observable scaling function that maps relative deviation to desired position */
                k       = .const(0.5),
                /** trader in question */
                trader  = .trader.SingleProxy()) : DesiredPositionStrategy
    {
        def DesiredPosition = trader~>Orderbook~>MidPrice~>EW(alpha)~>RelStdDev~>OnEveryDt(1.0) * k
    }

    /**
     *  Strategy believing that trader position should be proportional to 50 - RSI(asset)
     */
    type RSI_linear(
            /** alpha parameter for exponentially moving averages of up movements and down movements */
            alpha = 1./14.,
            /** observable scaling function that maps RSI deviation from 50 to the desired position */
            k = .const(-0.04),
            /** lag for calculating up and down movements */
            timeframe = 1.,
            /** trader in question */
            trader = .trader.SingleProxy()) : DesiredPositionStrategy
    {
        def DesiredPosition = (50. - trader~>Orderbook~>MidPrice~>RSI(timeframe, alpha)~>Value~>OnEveryDt(1.0)) * k
    }
}