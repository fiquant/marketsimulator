from marketsim.veusz_graph import Graph, showGraphs
import random
from marketsim.scheduler import Scheduler
from marketsim.order_queue import OrderBook
from marketsim.trader import LiquidityProvider, SASM_Trader
from marketsim import Side
from marketsim.indicator import AssetPrice, OnEveryDt, EWMA, TraderEfficiency, PnL

from marketsim import strategy

world = Scheduler()

book_A = OrderBook(tickSize=0.01, label="A")
book_B = OrderBook(tickSize=0.01, label="B")

price_graph = Graph("Price")
 
assetPrice_A = AssetPrice(book_A)
price_graph.addTimeSerie(assetPrice_A)

assetPrice_B = AssetPrice(book_B)
price_graph.addTimeSerie(assetPrice_B)

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

ewma_0_15 = EWMA(assetPrice_A, alpha=0.15)
ewma_0_015 = EWMA(assetPrice_A, alpha=0.015)
ewma_0_065 = EWMA(assetPrice_A, alpha=0.065)

price_graph.addTimeSerie(avg(assetPrice_A, alpha=0.15))
price_graph.addTimeSerie(avg(assetPrice_A, alpha=0.015), {r'PlotLine/bezierJoin':True})
price_graph.addTimeSerie(avg(assetPrice_A, alpha=0.65))

price_graph.addTimeSerie(avg(assetPrice_B, alpha=0.15))
price_graph.addTimeSerie(avg(assetPrice_B, alpha=0.015), {r'PlotLine/bezierJoin':True})
price_graph.addTimeSerie(avg(assetPrice_B, alpha=0.65))

liqVol = lambda: random.expovariate(.1)*5
seller_A = LiquidityProvider(book_A, Side.Sell, defaultValue=50., volumeDistr=liqVol)
buyer_A = LiquidityProvider(book_A, Side.Buy, defaultValue=50., volumeDistr=liqVol)

seller_B = LiquidityProvider(book_B, Side.Sell, defaultValue=150., volumeDistr=liqVol)
buyer_B = LiquidityProvider(book_B, Side.Buy, defaultValue=150., volumeDistr=liqVol)

dep_AB = strategy.Dependency(SASM_Trader(book_A, "AB"), book_B, factor=2)
dep_BA = strategy.Dependency(SASM_Trader(book_B, "BA"), book_A, factor=.5)

dep_AB.efficiency = TraderEfficiency([dep_AB.on_traded], dep_AB)
dep_BA.efficiency = TraderEfficiency([dep_BA.on_traded], dep_BA)

eff_graph = Graph("efficiency")
eff_graph.addTimeSerie(dep_AB.efficiency)
eff_graph.addTimeSerie(dep_BA.efficiency)
eff_graph.addTimeSerie(PnL(dep_AB))
eff_graph.addTimeSerie(PnL(dep_BA))

world.workTill(500)

showGraphs("dependency", [price_graph, eff_graph])
