@category = "Trader"
package trader
{
    /**
     *  Returns position of the trader
     *  It is negative if trader has sold more assets than has bought and
     *  positive otherwise
     */
    @python.intrinsic("trader.props.Position_Impl")
    def Position(trader =SingleProxy() : IAccount) : IObservable[Volume]

    /**
     *  Number of money owned by trader
     */
    @python.intrinsic("trader.props.Balance_Impl")
    def Balance(trader = SingleProxy() : IAccount) : IObservable[Price]

    /**
     *  Cumulative volume of orders sent to the market but haven't matched yet
     */
    @python.intrinsic("trader.props.PendingVolume_Impl")
    def PendingVolume(trader = SingleProxy() : IAccount) : IObservable[Volume]

    /**
     *  Returns traders eficiency. Under efficiency we understand trader balance if trader position was cleared
     */
    def Efficiency(trader = SingleProxy() : IAccount)
        = observable.Float(
                Balance(trader) +
                        orderbook.CumulativePrice(
                                orderbook.OfTrader(trader),
                                Position(trader)
                        )
        )

    /**
     *  Returns traders naive approximation of trader eficiency.
     *  It takes into account only the best price of the order queue
     */
    def RoughPnL(trader = SingleProxy() : IAccount)
        = observable.Float(
                Balance(trader) +
                        orderbook.NaiveCumulativePrice(
                                orderbook.OfTrader(trader),
                                Position(trader)
                        )
        )

    /**
     *  Returns first derivative of a moving average of the trader efficiency
     */
    def EfficiencyTrend(trader = SingleProxy() : IAccount, alpha = 0.15)
        = math.Derivative(
                math.EW.Avg(
                        Efficiency(trader),
                        alpha)
        )
}


