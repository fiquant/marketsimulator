import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, order,
                       scheduler, observable, veusz, mathutils)

from common import run 

def FundamentalValue(graph, world, books):

    book_A = books['Asset A']
    proxy_A = books['Proxy A']
     
    price_graph = graph("Price")
    assetPrice = observable.Price(book_A)
    
    avg = observable.avg    
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProvider(
                            volumeDistr=mathutils.constant(300),
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=mathutils.constant(10))),
                       "liquidity")
    
    fv = trader.SASM(book_A, 
                         strategy.FundamentalValue(
                            fundamentalValue = mathutils.constant(200),
                            volumeDistr = mathutils.constant(1)), 
                         "fv_200")

    fv_ex = trader.SASM(book_A, 
                         strategy.FundamentalValueEx(proxy_A,
                            fundamentalValue = mathutils.constant(200),
                            volumeDistr = mathutils.constant(1)), 
                         "fv_ex_200")
    
    price_graph += [assetPrice,
                    avg(assetPrice)]
    
    eff_graph = graph("efficiency")
    eff_graph += [observable.Efficiency(fv),
                  observable.VolumeTraded(fv)]
    eff_graph += [observable.Efficiency(fv_ex),
                  observable.VolumeTraded(fv_ex)]
    
    return [lp_A, fv, fv_ex], [price_graph, eff_graph]

if __name__ == '__main__':    
    run("fv_200_trader", FundamentalValue)
        
