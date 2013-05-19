import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, order, mathutils, Side,
                       scheduler, observable, veusz, registry, timeserie)

from common import run 

def Canceller(graph, world, books):

    book_A = books['Asset A']

    price_graph = graph("Price")
     
    amount_graph = graph("amount")
    
    def trader_ts():
        return {observable.VolumeTraded(trader.SASM_Proxy()) : amount_graph }
    
    def orderbook_ts():
        assetPrice = observable.AskPrice(orderbook.Proxy())
        avg = observable.avg
        return [timeserie.ToRecord(assetPrice, price_graph), 
                timeserie.ToRecord(avg(assetPrice), price_graph)]
       
    book_A.timeseries = orderbook_ts()
    
    lp = trader.SASM(book_A, 
                     strategy.LiquidityProviderSide(side = Side.Sell),
                     "LiquidityProvider-", timeseries = trader_ts())
    
    lp2 = trader.SASM(book_A, 
                     strategy.LiquidityProviderSide2(side = Side.Buy),
                     "LiquidityProviderSide2", timeseries = trader_ts())

    LP2 = trader.SASM(book_A, 
                     strategy.LiquidityProvider2(),
                     "LiquidityProvider2", timeseries = trader_ts())
    
    lp_ex = trader.SASM(book_A, 
                     strategy.LiquidityProviderEx(
                        orderFactory=order.WithExpiryFactory(
                                expirationDistr=mathutils.constant(1))),
                     "LiquidityProviderEx-", timeseries = trader_ts())
    
    lp_B = trader.SASM(book_A, 
                     strategy.LiquidityProviderSide(side = Side.Buy),
                     "LiquidityProviderBuy", timeseries = trader_ts())

    lp_C = trader.SASM(book_A, 
                       strategies = [
                            strategy.LiquidityProviderSide(side = Side.Sell),
                            strategy.Canceller()
                        ],
                       label = "LiquidityProviderWithCanceller",
                       timeseries = trader_ts())
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProviderSide(
                            side = Side.Sell,
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=mathutils.constant(10))),
                       "LiquidityProviderWithExpiry", 
                       timeseries = trader_ts())

    
    fv_trader = trader.SASM(book_A, 
                            strategy.FundamentalValue(fundamentalValue = mathutils.constant(1000)), 
                            "fv_1000",
                            timeseries = trader_ts())
    
    return [lp_A, lp2, LP2, lp, lp_C, lp_B, lp_ex, fv_trader], [price_graph, amount_graph]

if __name__ == '__main__':    
    run("canceller", Canceller)
