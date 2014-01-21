@category = "Volume function"

package strategy.position() {
    def DesiredPosition(desiredPosition = const(),
                        trader = trader.SingleProxy())
         = observable.Volume(desiredPosition-trader.Position(trader)-trader.PendingVolume(trader))
    
    def Bollinger_linear(alpha = 0.15,
                         k = const(0.5),
                         trader = trader.SingleProxy())
         = DesiredPosition(observable.OnEveryDt(1.0,math.EW.RelStdDev(orderbook.MidPrice(orderbook.OfTrader(trader)),alpha))*k,trader)
    
    def RSI_linear(alpha = 1.0/14.0,
                   k = const(-0.04),
                   timeframe = 1.0,
                   trader = trader.SingleProxy())
         = DesiredPosition(observable.OnEveryDt(1.0,50.0-math.RSI(orderbook.OfTrader(trader),timeframe,alpha))*k,trader)
}
