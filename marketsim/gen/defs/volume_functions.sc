package observable.volumefunc
{
    @python.observable("Volume function", "Dp_{%(trader)s}(%(desiredPosition)s)")
    def DesiredPosition(desiredPosition = constant(), trader = trader.SingleProxy())
        = desiredPosition - trader.Position(trader) - trader.PendingVolume(trader)

    def Bollinger_linear(alpha = 0.15, k = const(0.5), trader = trader.SingleProxy())
        = DesiredPosition(EW.RelStdDev(orderbook.MidPrice(orderbook.OfTrader(trader)), alpha) * k, trader)

    def RSI_linear(alpha = 1./14, k = const(-0.04), timeframe = 1., trader = trader.SingleProxy())
        = DesiredPosition((50 - orderbook.RSI(orderbook.OfTrader(trader), timeframe, alpha))* k, trader)
}