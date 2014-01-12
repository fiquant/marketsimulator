
package strategy {
    def RSI_linear(orderFactory = order._.signedVolume.MarketSigned(),
                   alpha = 1.0/14,
                   k = const(-0.04),
                   timeframe = 1.0)
         = Generic(orderFactory(observable.volumefunc.RSI_linear(alpha,k,timeframe)))
}
