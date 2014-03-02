
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
    {
        // defined at defs\strategies\sideprice.sc: 65.9
        def OneSide(side = side.Sell(),
                    sign = 1.0) = order.price.Limit(side,volume*1000)~>FloatingPrice(ticker~>Quote(start,end)+delta*sign~>BreaksAtChanges)~>Iceberg(volume)~>Strategy(event.After(0.0))
        
        // defined at defs\strategies\sideprice.sc: 72.9
        def TwoSides() = Combine(OneSide(side.Sell(),1.0),OneSide(side.Buy(),-1.0))
    }
    
    type MarketMaker(delta = 1.0,volume = 20.0)
    {
        // defined at defs\strategies\sideprice.sc: 77.9
        def OneSide(side = side.Sell(),
                    sign = 1.0) = order.price.Limit(side,volume*1000)~>FloatingPrice(orderbook.OfTrader()~>Queue(side)~>SafeSidePrice(100+delta*sign)/trader.Position()~>Atan/1000~>Exp~>OnEveryDt(0.9)~>BreaksAtChanges)~>Iceberg(volume)~>Strategy(event.After(0.0))
        
        // defined at defs\strategies\sideprice.sc: 86.9
        def TwoSides() = Combine(OneSide(side.Sell(),1.0),OneSide(side.Buy(),-1.0))
    }
}
