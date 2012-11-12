from marketsim.veusz_graph import Graph, showGraphs
from marketsim.scheduler import Scheduler
from marketsim.order_queue import OrderBook
from marketsim.trader import SASM_Trader
from marketsim import Side
from marketsim.indicator import AssetPrice, OnEveryDt, EWMA, VolumeTraded, TraderEfficiency, PnL

from marketsim import signal
from marketsim import strategy

world = Scheduler()

book_A = OrderBook(tickSize=0.01, label="A")

price_graph = Graph("Price")
 
assetPrice = AssetPrice(book_A)
price_graph.addTimeSerie(assetPrice)

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

price_graph.addTimeSerie(avg(assetPrice))

lp_A = strategy.LiquidityProvider(SASM_Trader(book_A), volumeDistr=lambda:1)
signal = signal.RandomWalk(initialValue=20, deltaDistr=lambda: -.1, label="signal")
trader = strategy.Signal(SASM_Trader(book_A, "signal"), signal)

price_graph.addTimeSerie(signal)
price_graph.addTimeSerie(VolumeTraded(trader))

trader.efficiency = TraderEfficiency([trader.on_traded], trader)

eff_graph = Graph("efficiency")
eff_graph.addTimeSerie(trader.efficiency)
eff_graph.addTimeSerie(PnL(trader))

world.workTill(500)

showGraphs("signal_trader", [price_graph, eff_graph])

