package strategy
{
    def RSI_linear( orderFactory = order.signedVolume.MarketSigned(),
                    alpha        = 1./14,
                    k            = const(-0.04),
                    timeframe    = 1.)

        = Generic(orderFactory(position.RSI_linear(alpha, k, timeframe)))

    def Bollinger_linear( orderFactory = order.signedVolume.MarketSigned(),
                          alpha        = 0.15,
                          k            = const(0.5))

        = Generic(orderFactory(position.Bollinger_linear(alpha, k)))
}