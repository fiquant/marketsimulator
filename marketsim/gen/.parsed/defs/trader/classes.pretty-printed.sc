@category = "Trader"

package trader() {
    // defined at defs\trader\classes.sc: 4.5
    /** A trader that trades a single asset on a single market
     */
    @python.intrinsic("trader.classes.SingleAsset_Impl")
    @label = "%(name)s"
    def SingleAsset(/** order book for the asset being traded */ orderBook : IOrderBook,
                    /** strategy run by the trader */ strategy = strategy.Empty(),
                    name = "-trader-",
                    /** current position of the trader (number of assets that it owns) */ amount = 0.0,
                    /** current trader balance (number of money units that it owns) */ PnL = 0.0,
                    /** defines what data should be gathered for the trader */ timeseries = [] : List[ITimeSerie]) : ISingleAssetTrader
    
    // defined at defs\trader\classes.sc: 21.5
    /** A trader that trades different assets
     *  It can be considered as a composition of single asset traders and multi asset strategies
     *  At the moment there is no way to instruct a multi asset strategy to trade only on subset of the assets
     */
    @python.intrinsic("trader.classes.MultiAsset_Impl")
    @label = "%(name)s"
    def MultiAsset(/** defines accounts for every asset to trade */ traders = [] : List[ISingleAssetTrader],
                   /** multi asset strategy run by the trader */ strategy = strategy.Arbitrage(),
                   name = "-trader-",
                   /** current trader balance (number of money units that it owns) */ PnL = 0.0,
                   /** defines what data should be gathered for the trader */ timeseries = [] : List[ITimeSerie]) : ITrader
    
    // defined at defs\trader\classes.sc: 38.5
    /** Phantom trader that is used to refer to the current trader
     *  (normally it is used to define trader properties and strategies)
     */
    @python.intrinsic("trader.proxy.Single_Impl")
    @label = "N/A"
    def SingleProxy() : ISingleAssetTrader
}
