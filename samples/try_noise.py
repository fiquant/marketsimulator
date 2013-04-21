import sys
sys.path.append(r'..')

from marketsim import (strategy, trader, orderbook, order, mathutils,
                       scheduler, observable, veusz, registry)

from common import run 

def Noise(graph, world, books):

    book_A = books['Asset A']

    price_graph = graph("Price")
     
    assetPrice = observable.Price(book_A)
    
    avg = observable.avg
    
    
    lp_A = trader.SASM(book_A, 
                       strategy.LiquidityProvider(
                            volumeDistr=mathutils.constant(2),
                            orderFactoryT=order.WithExpiryFactory(
                                expirationDistr=mathutils.constant(10))), 
                       "liquidity")
    
    noise_trader = trader.SASM(book_A, strategy.Noise(), "noise")
    noise_ex_trader = trader.SASM(book_A, strategy.NoiseEx(), "noise_ex")
    
    price_graph += [assetPrice,
                    avg(assetPrice)]
    
    eff_graph = graph("efficiency")
    eff_graph += [observable.Efficiency(noise_trader),
                  observable.PnL(noise_trader)]
    eff_graph += [observable.Efficiency(noise_ex_trader),
                  observable.PnL(noise_ex_trader)]
    
    return [lp_A, noise_trader, noise_ex_trader], [price_graph, eff_graph]


if __name__ == '__main__':    
    run("noise_trader", Noise)
