from marketsim.veusz_graph import Graph, showGraphs
from marketsim.indicator import AssetPrice, OnEveryDt, EWMA, VolumeTraded, TraderEfficiency, PnL

from marketsim import signal, strategy, trader, orderbook, scheduler

world = scheduler.create()

book_A = orderbook.Local(tickSize=0.01, label="A")

price_graph = Graph("Price")
 
assetPrice = AssetPrice(book_A)
price_graph.addTimeSerie(assetPrice)

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

price_graph.addTimeSerie(avg(assetPrice))

lp_A = strategy.LiquidityProvider(trader.SASM(book_A), volumeDistr=lambda:1).trader
signal = signal.RandomWalk(initialValue=20, deltaDistr=lambda: -.1, label="signal")
trader = strategy.Signal(trader.SASM(book_A, "signal"), signal).trader

price_graph.addTimeSerie(signal)
price_graph.addTimeSerie(VolumeTraded(trader))

trader.efficiency = TraderEfficiency([trader.on_traded], trader)

eff_graph = Graph("efficiency")
eff_graph.addTimeSerie(trader.efficiency)
eff_graph.addTimeSerie(PnL(trader))

world.workTill(500)

showGraphs("signal_trader", [price_graph, eff_graph])

