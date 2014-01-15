@category = "Trader"

package trader {
    /** A trader that trades a single asset on a single market
     */
    @python.intrinsic("trader.classes._SingleAsset_Impl")
    @label = "%(name)s"
    def SingleAsset(/** order book for the asset being traded */ orderBook : IOrderBook,
                    /** strategy run by the trader */ strategy = strategy.Noise(),
                    name = "-trader-",
                    /** current position of the trader (number of assets that it owns) */ amount = 0.0,
                    /** current trader balance (number of money units that it owns) */ PnL = 0.0,
                    timeseries = [] : List[ITimeSerie]) : ISingleAssetTrader
        
    
    @python.intrinsic("trader.classes._MultiAsset_Impl")
    @label = "%(name)s"
    def MultiAsset(traders = [] : List[ISingleAssetTrader],
                   /** strategy run by the trader */ strategy = strategy.Arbitrage(),
                   name = "-trader-",
                   /** current trader balance (number of money units that it owns) */ PnL = 0.0,
                   timeseries = [] : List[ITimeSerie]) : ITrader
        
    
    @python.intrinsic("trader.proxy._Single_Impl")
    @label = "N/A"
    def SingleProxy() : ISingleAssetTrader
        
}
@category = "Trader's"

package observable.trader {
    def SingleProxy = .trader.SingleProxy
    
    @python.intrinsic("trader.props.Position_Impl")
    def Position(trader = SingleProxy() : IAccount) : IObservable[Volume]
        
    
    @python.intrinsic("trader.props.Balance_Impl")
    def Balance(trader = SingleProxy() : IAccount) : IObservable[Price]
        
    
    @python.intrinsic("trader.props.PendingVolume_Impl")
    def PendingVolume(trader = SingleProxy() : IAccount) : IObservable[Volume]
        
    
    def Efficiency(trader = SingleProxy() : IAccount)
         = Observable(Balance(trader)+orderbook.CumulativePrice(orderbook.OfTrader(trader),Position(trader)))
    
    def RoughPnL(trader = SingleProxy() : IAccount)
         = Observable(Balance(trader)+orderbook.NaiveCumulativePrice(orderbook.OfTrader(trader),Position(trader)))
    
    def EfficiencyTrend(trader = SingleProxy() : IAccount,
                        alpha = 0.15)
         = Derivative(EW.Avg(Efficiency(trader),alpha))
}
