@category = "Trader"
package trader
{
    /**
     * A trader that trades a single asset on a single market
     */
    @python.intrinsic("trader.classes._SingleAsset_Impl")
    @label = "%(name)s"
    def SingleAsset(/** order book for the asset being traded */
                    orderBook : IOrderBook,
                    /** strategy run by the trader */
                    strategy    = strategy.Noise(),
                    name        = "-trader-",
                    /** current position of the trader (number of assets that it owns) */
                    amount      = 0.0,
                    /** current trader balance (number of money units that it owns) */
                    PnL         = 0.0,
                    timeseries  = [] : List[ITimeSerie]) : ISingleAssetTrader

    @python.intrinsic("trader.classes._MultiAsset_Impl")
    @label = "%(name)s"
    def MultiAsset( traders     = [] : List[ISingleAssetTrader],
                    /** strategy run by the trader */
                    strategy    = strategy.Arbitrage(),
                    name        = "-trader-",
                    /** current trader balance (number of money units that it owns) */
                    PnL         = 0.0,
                    timeseries  = [] : List[ITimeSerie]) : ITrader

    @python.intrinsic("trader.proxy._Single_Impl")
    @label = "N/A"
    def SingleProxy() : ISingleAssetTrader
}