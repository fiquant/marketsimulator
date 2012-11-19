from marketsim.veusz_graph import Graph, showGraphs
from marketsim import signal, strategy, trader, orderbook, scheduler, observable

world = scheduler.create()

book_A = orderbook.Local(tickSize=0.01, label="A")

price_graph = Graph("Price")
 
assetPrice = observable.Price(book_A)
price_graph.addTimeSerie(assetPrice)

avg = observable.avg

price_graph.addTimeSerie(avg(assetPrice))

lp_A = strategy.LiquidityProvider(trader.SASM(book_A), volumeDistr=lambda:1).trader
signal = signal.RandomWalk(initialValue=20, deltaDistr=lambda: -.1, label="signal")
trader = strategy.Signal(trader.SASM(book_A, "signal"), signal).trader

price_graph.addTimeSerie(signal)
price_graph.addTimeSerie(observable.VolumeTraded(trader))

eff_graph = Graph("efficiency")
eff_graph.addTimeSerie(observable.Efficiency(trader))
eff_graph.addTimeSerie(observable.PnL(trader))

world.workTill(500)

showGraphs("signal_trader", [price_graph, eff_graph])

