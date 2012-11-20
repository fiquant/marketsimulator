import random
from marketsim import strategy, trader, orderbook, scheduler, observable, veusz

world = scheduler.create()

avg = observable.avg
book_A = orderbook.Local(tickSize=0.01, label="A")

price_graph = veusz.Graph("Price")
 
assetPrice = observable.Price(book_A)

price_graph += [assetPrice,
                avg(assetPrice, alpha=0.15),
                avg(assetPrice, alpha=0.015),
                avg(assetPrice, alpha=0.65)]

def volume(v):
    return lambda: v*random.expovariate(.1)

lp_A = strategy.LiquidityProvider(\
        trader.SASM(book_A, "A"), volumeDistr=volume(10)).trader
lp_a = strategy.LiquidityProvider(\
        trader.SASM(book_A, "a"), volumeDistr=volume(1)).trader

spread_graph = veusz.Graph("Bid-Ask Spread")

spread_graph += [observable.BidPrice(book_A), 
                 observable.AskPrice(book_A)]

eff_graph = veusz.Graph("efficiency")
eff_graph += [observable.Efficiency(lp_a),
              observable.PnL(lp_a)]

world.workTill(500)

veusz.render("liquidity", [price_graph, spread_graph, eff_graph])
