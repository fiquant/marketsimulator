@category = "Price function"

package strategy.price() {
    type LiquidityProvider(/** initial price which is taken if orderBook is empty */ initialValue = 100.0,/** defines multipliers for current asset price when price of
      *             order to create is calculated*/ priceDistr = .math.random.lognormvariate(0.0,0.1),/** asset in question */ book = .orderbook.OfTrader())
    {
        // defined at defs\strategies\sideprice.sc: 13.9
        def Price(side = .side.Sell() : IFunction[Side]) = book~>Queue(side)~>SafeSidePrice(initialValue)*priceDistr
        
        // defined at defs\strategies\sideprice.sc: 17.9
        def OneSideStrategy(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                            /** order factory function*/ orderFactory = order.side_price.Limit(),
                            /** side of orders to create */ side = .side.Sell()) = orderFactory(side,Price(side))~>Strategy(eventGen)
        
        // defined at defs\strategies\sideprice.sc: 27.9
        def Strategy(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                     /** order factory function*/ orderFactory = order.side_price.Limit()) = Combine(OneSideStrategy(eventGen,orderFactory,side.Sell()),OneSideStrategy(eventGen,orderFactory,side.Buy()))
    }
    
    type MarketData(/** Ticker of the asset */ ticker = "^GSPC",/** Start date in DD-MM-YYYY format */ start = "2001-1-1",/** End date in DD-MM-YYYY format */ end = "2010-1-1",/** Price difference between orders placed and underlying quotes */ delta = 1.0,/** Volume of Buy/Sell orders. Should be large compared to the volumes of other traders. */ volume = 1000.0)
    {
        // defined at defs\strategies\sideprice.sc: 58.9
        def OneSide(side = side.Sell(),
                    sign = 1.0) = order.price.Limit(side,volume*1000)~>FloatingPrice(ticker~>Quote(start,end)+delta*sign~>BreaksAtChanges)~>Iceberg(volume)~>Strategy(event.After(0.0))
        
        // defined at defs\strategies\sideprice.sc: 65.9
        def TwoSides() = Combine(OneSide(side.Sell(),1.0),OneSide(side.Buy(),-1.0))
    }
    
    type MarketMaker(delta = 1.0,volume = 20.0)
    {
        // defined at defs\strategies\sideprice.sc: 70.9
        def OneSide(side = side.Sell(),
                    sign = 1.0) = order.price.Limit(side,volume*1000)~>FloatingPrice(orderbook.OfTrader()~>Queue(side)~>SafeSidePrice(100+delta*sign)/trader.Position()~>Atan/1000~>Exp~>OnEveryDt(0.9)~>BreaksAtChanges)~>Iceberg(volume)~>Strategy(event.After(0.0))
        
        // defined at defs\strategies\sideprice.sc: 79.9
        def TwoSides() = Combine(OneSide(side.Sell(),1.0),OneSide(side.Buy(),-1.0))
    }
}
