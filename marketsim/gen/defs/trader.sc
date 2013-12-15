package observable.trader
{
    @python.intrinsic.function ("Proxies", "N/A", "trader.proxy._Single_Impl")
    def SingleProxy() : ISingleAssetTrader

    def Position(trader = SingleProxy()) => Float

    def Balance(trader = SingleProxy()) => Float

    def PendingVolume(trader = SingleProxy()) => Float

    def Efficiency(trader = SingleProxy())
        = Balance(trader) + orderbook.CumulativePrice(orderbook.OfTrader(trader), Position(trader))

    def EfficiencyTrend(trader = SingleProxy(), alpha = 0.15)
        = Derivative(EW.Avg(Efficiency(trader), alpha))
}