import sys
sys.path.append(r'../../..')

import random
from marketsim import strategy, orderbook, trader, scheduler, observable, veusz

with scheduler.create() as world:
    
    book_A = orderbook.Local(tickSize=0.01, label="A")
    book_B = orderbook.Local(tickSize=0.01, label="B")
    
    price_graph = veusz.Graph("Price")
     
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
    
    liqVol = lambda: random.expovariate(.1)*5
    t_A = trader.SASM(book_A, strategy=strategy.LiquidityProvider(defaultValue=50., volumeDistr=liqVol))
    t_B = trader.SASM(book_B, strategy=strategy.LiquidityProvider(defaultValue=150., volumeDistr=liqVol))
    
    dep_AB = strategy.Dependency(trader.SASM(book_A, "AB"), book_B, factor=2).trader
    dep_BA = strategy.Dependency(trader.SASM(book_B, "BA"), book_A, factor=.5).trader
    
    eff_graph = veusz.Graph("efficiency")
    eff_graph += [observable.Efficiency(dep_AB),
                  observable.Efficiency(dep_BA),
                  observable.PnL(dep_AB),
                  observable.PnL(dep_BA)]
    
    world.workTill(500)
    
    veusz.render("dependency", [price_graph, eff_graph])
