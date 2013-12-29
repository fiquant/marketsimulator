@category = "Volume function"
package observable.volumefunc
{
    @python.observable
    def DesiredPosition(desiredPosition = const(), trader = trader.SingleProxy())
        = desiredPosition - trader.Position(trader) - trader.PendingVolume(trader)

    @python.observable
    def Bollinger_linear(alpha = 0.15, k = const(0.5), trader = trader.SingleProxy())
        = DesiredPosition(OnEveryDt(1.0,
            EW.RelStdDev(orderbook.MidPrice(orderbook.OfTrader(trader)), alpha)) * k, trader)

    @python.observable
    def RSI_linear(alpha = 1./14., k = const(-0.04), timeframe = 1., trader = trader.SingleProxy())
        = DesiredPosition(OnEveryDt(1.,
            (50. - orderbook.RSI(orderbook.OfTrader(trader), timeframe, alpha))) * k, trader)
}