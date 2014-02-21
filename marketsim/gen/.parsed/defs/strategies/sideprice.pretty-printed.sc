
package strategy() {
    // defined at defs\strategies\sideprice.sc: 3.5
    /** Liquidity provider for one side
     */
    def LiquidityProviderSide(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                              /** order factory function*/ orderFactory = order.side_price.Limit(),
                              /** side of orders to create */ side = .side.Sell() : IFunction[Side],
                              /** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                              /** defines multipliers for current asset price when price of
                                *                    order to create is calculated*/ priceDistr = math.random.lognormvariate(0.0,0.1)) = Generic(orderFactory(side,price.LiquidityProvider(side,initialValue,priceDistr)),eventGen)
    
    // defined at defs\strategies\sideprice.sc: 28.5
    /** Liquidity provider for two sides
     */
    def LiquidityProvider(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                          /** order factory function*/ orderFactory = order.side_price.Limit(),
                          /** initial price which is taken if orderBook is empty */ initialValue = 100.0,
                          /** defines multipliers for current asset price when price of
                            *                    order to create is calculated*/ priceDistr = math.random.lognormvariate(0.0,0.1)) = Array([LiquidityProviderSide(eventGen,orderFactory,side.Sell(),initialValue,priceDistr),LiquidityProviderSide(eventGen,orderFactory,side.Buy(),initialValue,priceDistr)])
    
    package lp(/** initial price which is taken if orderBook is empty */ initialValue = 100.0,
               /** defines multipliers for current asset price when price of
                 *                    order to create is calculated*/ priceDistr = math.random.lognormvariate(0.0,0.1)) {
        // defined at defs\strategies\sideprice.sc: 53.9
        /** Liquidity provider for one side
         */
        def OneSide(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                    /** order factory function*/ orderFactory = order.side_price.Limit(),
                    /** side of orders to create */ side = .side.Sell() : IFunction[Side]) = Generic(orderFactory(side,price.LiquidityProvider(side,initialValue,priceDistr)),eventGen)
        
        // defined at defs\strategies\sideprice.sc: 72.9
        /** Liquidity provider for two sides
         */
        def TwoSide(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                    /** order factory function*/ orderFactory = order.side_price.Limit()) = Array([OneSide(eventGen,orderFactory,side.Sell()),OneSide(eventGen,orderFactory,side.Buy())])
    }
    
    // defined at defs\strategies\sideprice.sc: 86.5
    /** A Strategy that allows to drive the asset price based on historical market data
     *  by creating large volume orders for the given price.
     *
     *  Every time step of 1 in the simulation corresponds to a 1 day in the market data.
     *
     *  At each time step the previous Limit Buy/Sell orders are cancelled and new ones
     *  are created based on the next price of the market data.
     */
    def MarketData(/** Ticker of the asset */ ticker = "^GSPC",
                   /** Start date in DD-MM-YYYY format */ start = "2001-1-1",
                   /** End date in DD-MM-YYYY format */ end = "2010-1-1",
                   /** Price difference between orders placed and underlying quotes */ delta = 1.0,
                   /** Volume of Buy/Sell orders. Should be large compared to the volumes of other traders. */ volume = 1000.0) = Combine(Generic(order.Iceberg(volume,order.FloatingPrice(observable.BreaksAtChanges(observable.Quote(ticker,start,end)+delta),order.price.Limit(side.Sell(),volume*1000))),event.After(0.0)),Generic(order.Iceberg(volume,order.FloatingPrice(observable.BreaksAtChanges(observable.Quote(ticker,start,end)-delta),order.price.Limit(side.Buy(),volume*1000))),event.After(0.0)))
    
    // defined at defs\strategies\sideprice.sc: 124.5
    def MarketMaker(delta = 1.0,
                    volume = 20.0) = Combine(Generic(order.Iceberg(volume,order.FloatingPrice(observable.BreaksAtChanges(observable.OnEveryDt(orderbook.SafeSidePrice(orderbook.Asks(),100+delta)/math.Exp(math.Atan(trader.Position())/1000),0.9)),order.price.Limit(side.Sell(),volume*1000))),event.After(0.0)),Generic(order.Iceberg(volume,order.FloatingPrice(observable.BreaksAtChanges(observable.OnEveryDt(orderbook.SafeSidePrice(orderbook.Bids(),100-delta)/math.Exp(math.Atan(trader.Position())/1000),0.9)),order.price.Limit(side.Buy(),volume*1000))),event.After(0.0)))
}
