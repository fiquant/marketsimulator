
package strategy() {
    type MarketData(/** Ticker of the asset */ ticker = "^GSPC",/** Start date in DD-MM-YYYY format */ start = "2001-1-1",/** End date in DD-MM-YYYY format */ end = "2010-1-1",/** Price difference between orders placed and underlying quotes */ delta = 1.0,/** Volume of Buy/Sell orders. Should be large compared to the volumes of other traders. */ volume = 1000.0)
    {
        // defined at defs\strategies\sideprice.sc: 23.9
        def OneSide(side = side.Sell(),
                    sign = 1.0) = order.price.Limit(side,volume*1000)~>FloatingPrice(ticker~>Quote(start,end)+delta*sign~>BreaksAtChanges)~>Iceberg(volume)~>Strategy(event.After(0.0))
        
        // defined at defs\strategies\sideprice.sc: 30.9
        def TwoSides() = Combine(OneSide(side.Sell(),1.0),OneSide(side.Buy(),-1.0))
    }
    
    type MarketMaker(delta = 1.0,volume = 20.0)
    {
        // defined at defs\strategies\sideprice.sc: 35.9
        def OneSide(side = side.Sell(),
                    sign = 1.0) = order.price.Limit(side,volume*1000)~>FloatingPrice(orderbook.OfTrader()~>Queue(side)~>SafeSidePrice(100+delta*sign)/trader.Position()~>Atan/1000~>Exp~>OnEveryDt(0.9)~>BreaksAtChanges)~>Iceberg(volume)~>Strategy(event.After(0.0))
        
        // defined at defs\strategies\sideprice.sc: 44.9
        def TwoSides() = Combine(OneSide(side.Sell(),1.0),OneSide(side.Buy(),-1.0))
    }
}
