@category = "Trader"

package trader {
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
    /** Cumulative volume of orders sent to the market but haven't matched yet
     */
    @python.intrinsic("trader.props.PendingVolume_Impl")
    def PendingVolume(trader = SingleProxy() : IAccount) : IObservable[Volume]
    
    // defined at defs\trader\properties.sc: 24.5
    /** Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared
     */
    def Efficiency(trader = SingleProxy() : IAccount) = Balance(trader)+orderbook.CumulativePrice(orderbook.OfTrader(trader),Position(trader))
    
    // defined at defs\trader\properties.sc: 33.5
    /** Returns traders naive approximation of trader eficiency.
     *  It takes into account only the best price of the order queue
     */
    def RoughPnL(trader = SingleProxy() : IAccount) = Balance(trader)+orderbook.NaiveCumulativePrice(orderbook.OfTrader(trader),Position(trader))
    
    // defined at defs\trader\properties.sc: 43.5
    /** Returns first derivative of a moving average of the trader efficiency
     */
    def EfficiencyTrend(trader = SingleProxy() : IAccount,
                        alpha = 0.15) = math.Derivative(math.EW.Avg(Efficiency(trader),alpha))
}
