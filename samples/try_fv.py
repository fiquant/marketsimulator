import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, order, timeserie,
                       scheduler, observable, veusz, mathutils)

from common import run 

def FundamentalValue(graph, world, books):

    book_A = books['Asset A']
     
    price_graph = graph("Price")
    eff_graph = graph("efficiency")
    amount_graph = graph("amount")
     
    def trader_ts():
        thisTrader = trader.SASM_Proxy()
        return { observable.VolumeTraded(thisTrader) : amount_graph, 
                 observable.Efficiency(thisTrader)   : eff_graph }
    
    def orderbook_ts():
        assetPrice = observable.AskPrice(orderbook.Proxy())
        avg = observable.avg
        return [timeserie.ToRecord(assetPrice, price_graph), 
                timeserie.ToRecord(avg(assetPrice, alpha=0.15), price_graph),
                timeserie.ToRecord(avg(assetPrice, alpha=0.65), price_graph),
                timeserie.ToRecord(avg(assetPrice, alpha=0.015), price_graph)]
       
    book_A.timeseries = orderbook_ts()
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProvider(
                            volumeDistr=mathutils.constant(5),
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=mathutils.constant(10))),
                       "liquidity", 
                       timeseries = trader_ts())
    
    fv = trader.SASM(book_A, 
                     strategy.FundamentalValue(
                        fundamentalValue = mathutils.constant(200),
                        volumeDistr = mathutils.constant(1)), 
                     "fv_200", 
                     timeseries = trader_ts())

    fv_ex = trader.SASM(book_A, 
                         strategy.FundamentalValueEx(
                            fundamentalValue = mathutils.constant(200),
                            volumeDistr = mathutils.constant(1)), 
                         "fv_ex_200", 
                         timeseries = trader_ts())
        
    return [lp_A, fv, fv_ex], [price_graph, eff_graph, amount_graph]

if __name__ == '__main__':    
    run("fv_200_trader", FundamentalValue)
        
