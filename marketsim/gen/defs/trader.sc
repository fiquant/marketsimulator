@category = "Trader's"
package observable.trader
{
    @python.intrinsic("trader.proxy._Single_Impl")
    @label = "N/A"
    def SingleProxy() : ISingleAssetTrader

    @python.intrinsic("trader.props.Position_Impl")
    def Position(trader = SingleProxy()) : IObservable[Volume]

    @python.intrinsic("trader.props.Balance_Impl")
    def Balance(trader = SingleProxy()) : IObservable[Price]

    @python.intrinsic("trader.props.PendingVolume_Impl")
    def PendingVolume(trader = SingleProxy()) : IObservable[Volume]

    def Efficiency(trader = SingleProxy())
        = Observable(Balance(trader) + orderbook.CumulativePrice(orderbook.OfTrader(trader), Position(trader)))

    def RoughPnL(trader = SingleProxy())
        = Observable(Balance(trader) + orderbook.NaiveCumulativePrice(orderbook.OfTrader(trader), Position(trader)))

    def EfficiencyTrend(trader = SingleProxy(), alpha = 0.15)
        = Derivative(EW.Avg(Efficiency(trader), alpha))
}
