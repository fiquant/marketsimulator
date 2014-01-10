@category = "Strategy"
package strategies
{
    /**
     *  Generic strategy that wakes up on events given by *eventGen*,
     *  creates an order via *orderFactory* and sends the order to the market using its trader
     */
    @python.intrinsic("strategy.generic._Generic_Impl")
    def Generic(/** Event source making the strategy to wake up*/
                orderFactory : IOrderGenerator = order.Limit(),
                /** order factory function*/
                eventGen     : IEvent = observable.OnEveryDt()) : ISingleAssetStrategy
}
