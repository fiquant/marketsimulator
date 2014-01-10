@category = "Strategy"

package strategies {
    /** Generic strategy that wakes up on events given by *eventGen*,
     *  creates an order via *orderFactory* and sends the order to the market using its trader
     */
    @python.intrinsic("strategy.generic._Generic_Impl")
    def Generic(/** order factory function*/ orderFactory = order.Limit(),
                /** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent) : ISingleAssetStrategy
        
    
    /** Signal strategy listens to some discrete signal
     * and when the signal becomes more than some threshold the strategy starts to buy.
     * When the signal gets lower than -threshold the strategy starts to sell.
     */
    @python = "no"
    def Signal(/** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent,
               /** order factory function*/ orderFactory = order._.side.Market(),
               /** signal to be listened to */ signal = constant(0.0),
               /** threshold when the trader starts to act */ threshold = 0.7) : ISingleAssetStrategy
        
}
