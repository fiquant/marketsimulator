import sys, pickle
sys.path.append(r'..')

from marketsim import strategy, orderbook, trader, scheduler, observable, veusz, mathutils
from common import run

def Dependency(graph, world, books):

    book_A = books['Asset A']
    book_B = books['Asset B']
    
    proxy_A = books['Proxy A']
    proxy_B = books['Proxy B']

    price_graph = graph("Price")
     
    assetPrice_A = observable.Price(book_A)
    assetPrice_B = observable.Price(book_B)

    avg = observable.avg
    
    price_graph += [assetPrice_A,
                    avg(assetPrice_A, alpha=0.15),
                    avg(assetPrice_A, alpha=0.015),
                    avg(assetPrice_A, alpha=0.65),
                    assetPrice_B,
                    avg(assetPrice_B, alpha=0.15),
                    avg(assetPrice_B, alpha=0.015),
                    avg(assetPrice_B, alpha=0.65)]
    
    liqVol = mathutils.product(mathutils.rnd.expovariate(.1), mathutils.constant(10))
    t_A = trader.SASM(book_A, strategy.LiquidityProvider(defaultValue=50., volumeDistr=liqVol), "LiquidityProvider_A")
    t_B = trader.SASM(book_B, strategy.LiquidityProvider(defaultValue=150., volumeDistr=liqVol), "LiquidityProvider_B")
    
    dep_AB = trader.SASM(book_A, strategy.Dependency(book_B, factor=2), "A dependent on B")
    dep_BA = trader.SASM(book_B, strategy.Dependency(book_A, factor=.5), "B dependent on A")

    dep_AB_ex = trader.SASM(book_A, strategy.DependencyEx(proxy_A, book_B, factor=2), "A dependent on B ex")
    dep_BA_ex = trader.SASM(book_B, strategy.DependencyEx(proxy_B, book_A, factor=.5), "B dependent on A ex")
    
    eff_graph = graph("efficiency")
    eff_graph += [observable.Efficiency(dep_AB),
                  observable.Efficiency(dep_BA),
                  observable.VolumeTraded(dep_AB),
                  observable.VolumeTraded(dep_BA)]

    eff_graph += [observable.Efficiency(dep_AB_ex),
                  observable.Efficiency(dep_BA_ex),
                  observable.VolumeTraded(dep_AB_ex),
                  observable.VolumeTraded(dep_BA_ex)]

    return [t_A, t_B, dep_AB, dep_BA, dep_AB_ex, dep_BA_ex], [price_graph, eff_graph]

if __name__ == '__main__':    
    run("dependency", Dependency)