package observable.trader
{
    @python.intrinsic.function ("Proxies", "N/A", "trader.proxy._Single_Impl")
    def SingleProxy() : ISingleAssetTrader

    @python.intrinsic.observable("Trader's", "Amount_{%(trader)s}", "trader.props.Position_Impl")
    def Position(trader = SingleProxy()) => Float

    @python.intrinsic.observable("Trader's", "Balance_{%(trader)s}", "trader.props.Balance_Impl")
    def Balance(trader = SingleProxy()) => Float

    def PendingVolume(trader = SingleProxy()) => Float

    @python.observable("Trader's", "Efficiency_{%(trader)s}")
    def Efficiency(trader = SingleProxy())
        = Balance(trader) + orderbook.CumulativePrice(orderbook.OfTrader(trader), Position(trader))

    def EfficiencyTrend(trader = SingleProxy(), alpha = 0.15)
        = Derivative(EW.Avg(Efficiency(trader), alpha))
}