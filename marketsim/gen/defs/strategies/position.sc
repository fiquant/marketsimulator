package strategy
{
    /**
     *  Strategy believing that trader position should be proportional to 50 - RSI(asset)
     */
    def RSI_linear( /** order factory function */
                    orderFactory = order.signedVolume.MarketSigned(),
                    /** alpha parameter for exponentially moving averages of up movements and down movements */
                    alpha        = 1./14,
                    /** observable scaling function that maps RSI deviation from 50 to the desired position */
                    k            = const(-0.04),
                    /** lag for calculating up and down movements */
                    timeframe    = 1.)

        = (orderFactory(position.RSI_linear(alpha, k, timeframe)))~>Strategy

    /**
     *  Strategy believing that trader position should be proportional to the relative standard deviation of its price
     */
    def Bollinger_linear(   /** order factory function */
                            orderFactory = order.signedVolume.MarketSigned(),
                            /** alpha parameter for exponentially weighted moving everage and variance */
                            alpha        = 0.15,
                            /** observable scaling function that maps relative deviation to desired position */
                            k            = const(0.5))

        = (orderFactory(position.Bollinger_linear(alpha, k)))~>Strategy
}