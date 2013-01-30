import sys
sys.path.append(r'..')

import random
from marketsim import strategy, orderbook, trader, scheduler, observable, veusz, registry

new = registry.new
setAttr = registry.setAttr

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
    t_A = trader.SASM(book_A, strategy.LiquidityProvider(defaultValue=50., volumeDistr=liqVol))
    t_B = trader.SASM(book_B, strategy.LiquidityProvider(defaultValue=150., volumeDistr=liqVol))
    
    dep_AB = trader.SASM(book_A, strategy.Dependency(book_B, factor=2), "AB")
    dep_BA = trader.SASM(book_B, strategy.Dependency(book_A, factor=.5), "BA")
    
    registry.insert(dep_AB)
    registry.insert(dep_BA)
    
    for k,v in registry.dumpall().iteritems():
        print k, v
        
    registry.setAttr(dep_AB.strategies[0], 'bookToDependOn', book_B)
    
    eff_graph = veusz.Graph("efficiency")
    eff_graph += [observable.Efficiency(dep_AB),
                  observable.Efficiency(dep_BA),
                  observable.PnL(dep_AB),
                  observable.PnL(dep_BA)]
    
    registry.instance.reset()
    
    world.workTill(500)
    
    veusz.render("dependency", [price_graph, eff_graph])
