import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, order,
                       scheduler, observable, veusz, mathutils)

from common import run 

def FundamentalValue(graph, world, books):

    book_A = books['Asset A']
     
    price_graph = graph("Price")
    assetPrice = observable.Price(book_A)
    
    avg = observable.avg    
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProvider(
                            volumeDistr=mathutils.constant(1),
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=mathutils.constant(10))),
                       "liquidity")
    
    fv = trader.SASM(book_A, 
                         strategy.FundamentalValue(
                            fundamentalValue = mathutils.constant(200)), 
                         "fv_200")
    
    price_graph += [assetPrice,
                    avg(assetPrice)]
    
    eff_graph = graph("efficiency")
    eff_graph += [observable.Efficiency(fv),
                  observable.PnL(fv)]
    
    return [lp_A, fv], [price_graph, eff_graph]

if __name__ == '__main__':    
    run("fv_200_trader", FundamentalValue)
        
