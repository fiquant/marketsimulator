@category = "Strategy"
package strategies
{
    /**
     *  Generic strategy that wakes up on events given by *eventGen*,
     *  creates an order via *orderFactory* and sends the order to the market using its trader
     */
    @python.intrinsic("strategy.generic._Generic_Impl")
    def Generic(/** order factory function*/
                orderFactory = order.Limit(),
                /** Event source making the strategy to wake up*/
                eventGen     = observable.OnEveryDt() : IEvent) : ISingleAssetStrategy

    /**
     * Signal strategy listens to some discrete signal
     * and when the signal becomes more than some threshold the strategy starts to buy.
     * When the signal gets lower than -threshold the strategy starts to sell.
     */
    def Signal(/** Event source making the strategy to wake up*/
               eventGen     = observable.OnEveryDt() : IEvent,
               /** order factory function*/
               orderFactory = order._.side.Market(),
               /** signal to be listened to */
               signal       = constant(0.),
               /** threshold when the trader starts to act */
               threshold    = 0.7)
        =
            Generic(orderFactory(observable.sidefunc.Signal(signal, threshold)), eventGen)

    /**
     * Trend follower can be considered as a sort of a signal strategy
     * where the *signal* is a trend of the asset.
     * Under trend we understand the first derivative of some moving average of asset prices.
     * If the derivative is positive, the trader buys; if negative - it sells.
     * Since moving average is a continuously changing signal, we check its
     * derivative at moments of time given by *eventGen*.
     */
    def TrendFollower(  /** Event source making the strategy to wake up*/
                        eventGen     = observable.OnEveryDt() : IEvent,
                        /** order factory function*/
                        orderFactory = order._.side.Market(),
                        /** parameter |alpha| for exponentially weighted moving average */
                        ewma_alpha   = 0.15,
                        /** threshold when the trader starts to act */
                        threshold    = 0.)
        =
            Generic(orderFactory(observable.sidefunc.TrendFollower(ewma_alpha, threshold)), eventGen)
}
