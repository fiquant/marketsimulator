import random
from marketsim import strategy, orderbook, trader, scheduler, observable, veusz

world = scheduler.create()

book_A = orderbook.Local(tickSize=0.01, label="A")
book_B = orderbook.Local(tickSize=0.01, label="B")

price_graph = veusz.Graph("Price")
 
assetPrice_A = observable.Price(book_A)
price_graph.addTimeSerie(assetPrice_A)

assetPrice_B = observable.Price(book_B)
price_graph.addTimeSerie(assetPrice_B)

avg = observable.avg

price_graph += [avg(assetPrice_A, alpha=0.15),
                avg(assetPrice_A, alpha=0.015),
                avg(assetPrice_A, alpha=0.65),
                avg(assetPrice_B, alpha=0.15),
                avg(assetPrice_B, alpha=0.015),
                avg(assetPrice_B, alpha=0.65)]

liqVol = lambda: random.expovariate(.1)*5
lp_A = strategy.LiquidityProvider(trader.SASM(book_A), defaultValue=50., volumeDistr=liqVol).trader
lp_B = strategy.LiquidityProvider(trader.SASM(book_B), defaultValue=150., volumeDistr=liqVol).trader

dep_AB = strategy.Dependency(trader.SASM(book_A, "AB"), book_B, factor=2).trader
dep_BA = strategy.Dependency(trader.SASM(book_B, "BA"), book_A, factor=.5).trader

eff_graph = veusz.Graph("efficiency")
eff_graph += [observable.Efficiency(dep_AB),
              observable.Efficiency(dep_BA),
              observable.PnL(dep_AB),
              observable.PnL(dep_BA)]

world.workTill(500)

veusz.render("dependency", [price_graph, eff_graph])
