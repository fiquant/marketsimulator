from marketsim.veusz_graph import Graph, showGraphs
import random
from marketsim import strategy, trader, orderbook, scheduler, observable

world = scheduler.create()

avg = observable.avg
book_A = orderbook.Local(tickSize=0.01, label="A")

price_graph = Graph("Price")
 
assetPrice = observable.Price(book_A)

price_graph.addTimeSeries([\
    assetPrice,
    avg(assetPrice, alpha=0.15),
    avg(assetPrice, alpha=0.015),
    avg(assetPrice, alpha=0.65)])

def volume(v):
    return lambda: v*random.expovariate(.1)

lp_A = strategy.LiquidityProvider(trader.SASM(book_A, "A"), volumeDistr=volume(10)).trader
lp_a = strategy.LiquidityProvider(trader.SASM(book_A, "a"), volumeDistr=volume(1)).trader

spread_graph = Graph("Bid-Ask Spread")

spread_graph.addTimeSerie(observable.BidPrice(book_A))
spread_graph.addTimeSerie(observable.AskPrice(book_A))

eff_graph = Graph("efficiency")
eff_graph.addTimeSerie(observable.Efficiency(lp_a))
eff_graph.addTimeSerie(observable.PnL(lp_a))

world.workTill(500)

showGraphs("liquidity", [price_graph, spread_graph, eff_graph])
