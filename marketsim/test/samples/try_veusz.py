import sys
sys.path.append(r'../../..')

import random
import threading
from marketsim import strategy, trader, orderbook, scheduler, observable, veusz

price_graph = veusz.Graph("Price")
spread_graph = veusz.Graph("Bid-Ask Spread")
eff_graph = veusz.Graph("efficiency")

N = 10

worlds = [scheduler.create() for i in range(N)]

def createSimulation(world, i):
    global price_graph, spread_graph, eff_graph
    
    with world:
        avg = observable.avg
        book_A = orderbook.Local(tickSize=0.01, label="A"+i)
        
        assetPrice = observable.Price(book_A)
        
        price_graph += [assetPrice,
                        avg(assetPrice, alpha=0.15),
                        avg(assetPrice, alpha=0.015),
                        avg(assetPrice, alpha=0.65)]
        
        def volume(v):
            return lambda: v*random.expovariate(.1)
        
        lp_A = strategy.LiquidityProvider(\
                trader.SASM(book_A, "A"+i), volumeDistr=volume(10)).trader
        lp_a = strategy.LiquidityProvider(\
                trader.SASM(book_A, "a"+i), volumeDistr=volume(1)).trader
        
        spread_graph += [observable.BidPrice(book_A), 
                         observable.AskPrice(book_A)]
        
        eff_graph += [observable.Efficiency(lp_a),
                      observable.PnL(lp_a)]

for i in range(N):
    createSimulation(worlds[i], str(i))

threads = [threading.Thread(target=world.workTill, args=(500,)) for world in worlds]

for t in threads:
    t.start()

for t in threads:
    t.join()

veusz.render("liquidity", [price_graph, spread_graph, eff_graph])
