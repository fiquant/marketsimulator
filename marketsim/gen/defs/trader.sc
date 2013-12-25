@category = "Trader's"
package observable.trader
{
    @python.intrinsic("trader.proxy._Single_Impl")
    @label = "N/A"
    def SingleProxy() : ISingleAssetTrader

    @python.intrinsic("trader.props.Position_Impl")
    @label = "Amount_{%(trader)s}"
    def Position(trader = SingleProxy()) : IObservable_Float

    @python.intrinsic("trader.props.Balance_Impl")
    @label = "Balance_{%(trader)s}"
    def Balance(trader = SingleProxy()) : IObservable_Float

    @python.intrinsic("trader.props.PendingVolume_Impl")
    @label = "PendingVolume_{%(trader)s}"
    def PendingVolume(trader = SingleProxy()) : IObservable_Float

    @python.observable
    @label = "Efficiency_{%(trader)s}"
    def Efficiency(trader = SingleProxy())
        = Observable(Balance(trader) + orderbook.CumulativePrice(orderbook.OfTrader(trader), Position(trader)))

    @python.observable
    @label = "RoughPnL_{%(trader)s}"
    def RoughPnL(trader = SingleProxy())
        = Observable(Balance(trader) + orderbook.NaiveCumulativePrice(orderbook.OfTrader(trader), Position(trader)))

    @python
    @label = "EfficiencyTrend_{%(trader)s}"
    def EfficiencyTrend(trader = SingleProxy(), alpha = 0.15)
        = Derivative(EW.Avg(Efficiency(trader), alpha))
}