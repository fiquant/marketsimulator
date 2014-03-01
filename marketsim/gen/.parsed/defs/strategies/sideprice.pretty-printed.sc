
package strategy() {
    // defined at defs\strategies\sideprice.sc: 3.5
    /** Liquidity provider for one side
     */
    def LiquidityProviderSide(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                              /** order factory function*/ orderFactory = order.side_price.Limit(),
                              /** side of orders to create */ side = .side.Sell() : IFunction[Side],
                              /** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                              /** defines multipliers for current asset price when price of
                                *                    order to create is calculated*/ priceDistr = math.random.lognormvariate(0.0,0.1)) = orderFactory(side,price.LiquidityProvider(side,initialValue,priceDistr))~>Strategy(eventGen)
    
    // defined at defs\strategies\sideprice.sc: 26.5
    /** Liquidity provider for two sides
     */
    def LiquidityProvider(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                          /** order factory function*/ orderFactory = order.side_price.Limit(),
                          /** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                          /** defines multipliers for current asset price when price of
                            *                    order to create is calculated*/ priceDistr = math.random.lognormvariate(0.0,0.1)) = Array([LiquidityProviderSide(eventGen,orderFactory,side.Sell(),initialValue,priceDistr),LiquidityProviderSide(eventGen,orderFactory,side.Buy(),initialValue,priceDistr)])
    
    type MarketData(/** Ticker of the asset */ ticker = "^GSPC",/** Start date in DD-MM-YYYY format */ start = "2001-1-1",/** End date in DD-MM-YYYY format */ end = "2010-1-1",/** Price difference between orders placed and underlying quotes */ delta = 1.0,/** Volume of Buy/Sell orders. Should be large compared to the volumes of other traders. */ volume = 1000.0)
    
    // defined at defs\strategies\sideprice.sc: 65.5
    def OneSide(x = MarketData(),
                side = side.Sell(),
                sign = 1.0) = order.price.Limit(side,x~>Volume*1000)~>FloatingPrice(x~>Ticker~>Quote(x~>Start,x~>End)+x~>Delta*sign~>BreaksAtChanges)~>Iceberg(x~>Volume)~>Strategy(event.After(0.0))
    
    // defined at defs\strategies\sideprice.sc: 72.5
    def TwoSides(x = MarketData()) = Combine(x~>OneSide(side.Sell(),1.0),x~>OneSide(side.Buy(),-1.0))
    
    // defined at defs\strategies\sideprice.sc: 74.5
    def MarketMaker(delta = 1.0,
                    volume = 20.0) = Combine(order.price.Limit(side.Sell(),volume*1000)~>FloatingPrice(orderbook.Asks()~>SafeSidePrice(100+delta)/trader.Position()~>Atan/1000~>Exp~>OnEveryDt(0.9)~>BreaksAtChanges)~>Iceberg(volume)~>Strategy(event.After(0.0)),order.price.Limit(side.Buy(),volume*1000)~>FloatingPrice(orderbook.Bids()~>SafeSidePrice(100-delta)/trader.Position()~>Atan/1000~>Exp~>OnEveryDt(0.9)~>BreaksAtChanges)~>Iceberg(volume)~>Strategy(event.After(0.0)))
}
