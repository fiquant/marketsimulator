@category = "Trader"

package trader() {
    @python.intrinsic("trader.props.Position_Impl")
    def Position(trader = SingleProxy() : IAccount) : IObservable[Volume]
        
    
    @python.intrinsic("trader.props.Balance_Impl")
    def Balance(trader = SingleProxy() : IAccount) : IObservable[Price]
        
    
    @python.intrinsic("trader.props.PendingVolume_Impl")
    def PendingVolume(trader = SingleProxy() : IAccount) : IObservable[Volume]
        
    
    def Efficiency(trader = SingleProxy() : IAccount)
         = observable.Float(Balance(trader)+orderbook.CumulativePrice(orderbook.OfTrader(trader),Position(trader)))
    
    def RoughPnL(trader = SingleProxy() : IAccount)
         = observable.Float(Balance(trader)+orderbook.NaiveCumulativePrice(orderbook.OfTrader(trader),Position(trader)))
    
    def EfficiencyTrend(trader = SingleProxy() : IAccount,
                        alpha = 0.15)
         = math.Derivative(math.EW.Avg(Efficiency(trader),alpha))
}
