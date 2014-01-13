@category = "Strategy"
package strategy
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

    @python.intrinsic("strategy.combine._Combine_Impl")
    def Combine(A = Noise(), B = Noise()) : ISingleAssetStrategy


    @python.intrinsic("strategy.canceller._Canceller_Impl")
    def Canceller(cancellationIntervalDistr = mathutils.rnd.expovariate(1.)) : ISingleAssetStrategy

    @python.intrinsic("strategy.arbitrage._Arbitrage_Impl")
    def Arbitrage() : IMultiAssetStrategy
}
