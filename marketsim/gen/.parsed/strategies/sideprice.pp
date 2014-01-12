
package strategy {
    /** Liquidity provider for one side
     */
    def LiquidityProviderSide(/** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent,
                              /** order factory function*/ orderFactory = order._.side_price.Limit(),
                              /** side of orders to create */ side = .side.Sell(),
                              /** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                              /** defines multipliers for current asset price when price of
                                *                    order to create is calculated*/ priceDistr = mathutils.rnd.lognormvariate(0.0,0.1))
         = Generic(orderFactory(side,observable.pricefunc.LiquidityProvider(side,initialValue,priceDistr)),eventGen)
    
    /** Liquidity provider for two sides
     */
    def LiquidityProvider(/** Event source making the strategy to wake up*/ eventGen = observable.OnEveryDt() : IEvent,
                          /** order factory function*/ orderFactory = order._.side_price.Limit(),
                          /** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                          /** defines multipliers for current asset price when price of
                            *                    order to create is calculated*/ priceDistr = mathutils.rnd.lognormvariate(0.0,0.1))
         = Combine(LiquidityProviderSide(eventGen,orderFactory,side.Sell(),initialValue,priceDistr),LiquidityProviderSide(eventGen,orderFactory,side.Buy(),initialValue,priceDistr))
}
