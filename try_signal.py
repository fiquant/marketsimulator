from marketsim.veusz_graph import Graph, showGraphs
import math
from marketsim.scheduler import world
from marketsim.order_queue import OrderBook
from marketsim.trader import LiquidityProvider, Signal, SignalTrader
from marketsim import Side
from marketsim.indicator import AssetPrice, BidPrice, AskPrice, OnEveryDt, EWMA, VolumeTraded

book_A = OrderBook(tickSize=0.01, label="A")

price_graph = Graph("Price")
 
assetPrice = AssetPrice(book_A)
price_graph.addTimeSerie(assetPrice)

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha=0.15))

price_graph.addTimeSerie(avg(assetPrice))

seller_A = LiquidityProvider(book_A, Side.Sell, volumeDistr=lambda:1)
buyer_A = LiquidityProvider(book_A, Side.Buy, volumeDistr=lambda:1)
signal = Signal(initialValue=20, deltaDistr=lambda: -.1, label="signal")
trader = SignalTrader(book_A, signal)

price_graph.addTimeSerie(signal)
price_graph.addTimeSerie(VolumeTraded(trader))
world.workTill(500)

showGraphs("signal_trader", [price_graph])

world.reset()