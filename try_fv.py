from marketsim.veusz_graph import Graph, showGraphs
from marketsim.scheduler import Scheduler
from marketsim.order_queue import OrderBook
from marketsim.trader import LiquidityProvider, FVTrader
from marketsim import Side
from marketsim.indicator import AssetPrice, OnEveryDt, EWMA, TraderEfficiency, PnL, VolumeTraded
from marketsim.order import VirtualMarketOrderT

world = Scheduler()

book_A = OrderBook(tickSize=0.01, label="A")

price_graph = Graph("Price")
 
assetPrice = AssetPrice(book_A)
price_graph.addTimeSerie(assetPrice)

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

price_graph.addTimeSerie(avg(assetPrice))

seller_A = LiquidityProvider(book_A, Side.Sell, volumeDistr=lambda: 20)
buyer_A = LiquidityProvider(book_A, Side.Buy, volumeDistr=lambda: 20)

trader_200 = FVTrader(book_A, fundamentalValue=lambda: 200., volumeDistr=lambda: 5)
trader_150 = FVTrader(book_A, fundamentalValue=lambda: 150., volumeDistr=lambda: 2)

trader_200.label = "t200"
trader_150.label = "t150"

virtual_160 = FVTrader(book_A, fundamentalValue=lambda: 160., orderFactory=VirtualMarketOrderT, volumeDistr=lambda: 1)
virtual_170 = FVTrader(book_A, fundamentalValue=lambda: 170., orderFactory=VirtualMarketOrderT, volumeDistr=lambda: 1)
virtual_180 = FVTrader(book_A, fundamentalValue=lambda: 180., orderFactory=VirtualMarketOrderT, volumeDistr=lambda: 1)

virtual_160.label = "v160"
virtual_170.label = "v170"
virtual_180.label = "v180"

def efficiency(trader):
    return TraderEfficiency([trader.on_traded], trader)

def addToGraph(graph, traders):
    for t in traders:
        eff_graph.addTimeSerie(efficiency(t))
        eff_graph.addTimeSerie(PnL(t))
        eff_graph.addTimeSerie(VolumeTraded(t))
        

eff_graph = Graph("efficiency")
addToGraph(eff_graph, [trader_150, trader_200, virtual_160, virtual_170, virtual_180])

world.workTill(1500)

showGraphs("fv_trader", [price_graph, eff_graph])
