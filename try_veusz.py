from marketsim.veusz_graph import Graph, showGraphs
from marketsim.scheduler import Scheduler, Timer
from marketsim.order_queue import OrderBook
from marketsim.trader import LiquidityProvider
from marketsim import Side
from marketsim.indicator import AssetPrice, BidPrice, AskPrice, OnEveryDt, EWMA, TraderEfficiency, PnL
from random import random, expovariate

world = Scheduler()

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

book_A = OrderBook(tickSize=0.01, label="A")

price_graph = Graph("Price")
 
assetPrice = AssetPrice(book_A)

price_graph.addTimeSeries([\
    assetPrice,
    avg(assetPrice, alpha=0.15),
    avg(assetPrice, alpha=0.015),
    avg(assetPrice, alpha=0.65)])

def volume(v):
    return lambda: v*expovariate(.1)

seller_A = LiquidityProvider(book_A, Side.Sell, volumeDistr=volume(10))
buyer_A = LiquidityProvider(book_A, Side.Buy, volumeDistr=volume(10))

seller_a = LiquidityProvider(book_A, Side.Sell, volumeDistr=volume(1))
buyer_a = LiquidityProvider(book_A, Side.Buy, volumeDistr=volume(1))

spread_graph = Graph("Bid-Ask Spread")

spread_graph.addTimeSerie(BidPrice(book_A))
spread_graph.addTimeSerie(AskPrice(book_A))

seller_a.label = "seller_a"
seller_a.efficiency = TraderEfficiency([seller_a.on_traded], seller_a)

eff_graph = Graph("efficiency")
eff_graph.addTimeSerie(seller_a.efficiency)
eff_graph.addTimeSerie(PnL(seller_a))

buyer_a.label = "buyer_a"
buyer_a.efficiency = TraderEfficiency([buyer_a.on_traded], buyer_a)

eff_graph.addTimeSerie(buyer_a.efficiency)
eff_graph.addTimeSerie(PnL(buyer_a))

world.workTill(500)

showGraphs("liquidity", [price_graph, spread_graph, eff_graph])
