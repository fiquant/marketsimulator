@category = "Trader"

package trader() {
    // defined at defs\trader\properties.sc: 4.5
    /** Returns position of the trader
     *  It is negative if trader has sold more assets than has bought and
     *  positive otherwise
     */
    @python.intrinsic("trader.props.Position_Impl")
    def Position(trader = SingleProxy() : IAccount) : IObservable[Volume]
    
    // defined at defs\trader\properties.sc: 12.5
    /** Number of money owned by trader
     */
    @python.intrinsic("trader.props.Balance_Impl")
    def Balance(trader = SingleProxy() : IAccount) : IObservable[Price]
    
    // defined at defs\trader\properties.sc: 18.5
    def PerSharePrice(trader = SingleProxy() : IAccount) = 0-trader~>Balance/trader~>Position
    
    // defined at defs\trader\properties.sc: 20.5
    /** Cumulative volume of orders sent to the market but haven't matched yet
     */
    @python.intrinsic("trader.props.PendingVolume_Impl")
    def PendingVolume(trader = SingleProxy() : IAccount) : IObservable[Volume]
    
    // defined at defs\trader\properties.sc: 26.5
    /** Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared
     */
    def Efficiency(trader = SingleProxy() : IAccount) = trader~>Balance+trader~>Orderbook~>CumulativePrice(trader~>Position)
    
    // defined at defs\trader\properties.sc: 32.5
    /** Returns traders naive approximation of trader eficiency.
     *  It takes into account only the best price of the order queue
     */
    def RoughPnL(trader = SingleProxy() : IAccount) = trader~>Balance+trader~>Orderbook~>NaiveCumulativePrice(trader~>Position)
    
    // defined at defs\trader\properties.sc: 39.5
    /** Returns first derivative of a moving average of the trader efficiency
     */
    def EfficiencyTrend(trader = SingleProxy() : IAccount,
                        alpha = 0.15) = trader~>Efficiency~>EW(alpha)~>Avg~>Derivative
    
    // defined at defs\trader\properties.sc: 46.5
    @python.intrinsic("trader.props.OnTraded_Impl")
    def OnTraded(trader = SingleProxy() : IAccount) : IEvent
    
    // defined at defs\trader\properties.sc: 49.5
    @python.intrinsic("trader.props.OnOrderMatched_Impl")
    def OnOrderMatched(trader = SingleProxy() : IAccount) : IEvent
}
