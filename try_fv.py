from marketsim.veusz_graph import Graph, showGraphs
from marketsim.scheduler import Scheduler
from marketsim.order_queue import OrderBook
from marketsim.trader import LiquidityProvider, FVTrader, TrendFollower
from marketsim import Side
from marketsim.indicator import AssetPrice, OnEveryDt, ewma, dEWMA, EWMA, TraderEfficiency, \
    PnL, VolumeTraded, InstEfficiency
from marketsim.order import VirtualMarketOrderT

world = Scheduler()

book_A = OrderBook(tickSize=0.01, label="A")

price_graph = Graph("Price")
 
assetPrice = AssetPrice(book_A)
price_graph.addTimeSerie(assetPrice)

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

def trend(source, alpha=0.015):
    return OnEveryDt(1, dEWMA(source, alpha))

price_graph.addTimeSerie(avg(assetPrice))

seller_A = LiquidityProvider(book_A, Side.Sell, volumeDistr=lambda: 20)
buyer_A = LiquidityProvider(book_A, Side.Buy, volumeDistr=lambda: 20)

trader_200 = FVTrader(book_A, fundamentalValue=lambda: 200., volumeDistr=lambda: 5)
trader_150 = FVTrader(book_A, fundamentalValue=lambda: 150., volumeDistr=lambda: 4)

trader_200.label = "t200"
trader_150.label = "t150"

virtual_160 = FVTrader(book_A, fundamentalValue=lambda: 160., orderFactory=VirtualMarketOrderT, volumeDistr=lambda: 1)
virtual_170 = FVTrader(book_A, fundamentalValue=lambda: 170., orderFactory=VirtualMarketOrderT, volumeDistr=lambda: 1)
virtual_180 = FVTrader(book_A, fundamentalValue=lambda: 180., orderFactory=VirtualMarketOrderT, volumeDistr=lambda: 1)
virtual_190 = FVTrader(book_A, fundamentalValue=lambda: 190., orderFactory=VirtualMarketOrderT, volumeDistr=lambda: 1)

virtual_160.label = "v160"
virtual_170.label = "v170"
virtual_180.label = "v180"
virtual_190.label = "v190"

tf = TrendFollower(book_A, average=ewma(0.015), volumeDistr=lambda: 5)
tf.label = "TF"

tf_0_15 = TrendFollower(book_A, orderFactory=VirtualMarketOrderT, average=ewma(0.15))
tf_0_015 = TrendFollower(book_A, orderFactory=VirtualMarketOrderT, average=ewma(0.015))

tf_0_15.label = "tf0.15"
tf_0_015.label = "tf0.015"

def efficiency(trader):
    return TraderEfficiency([trader.on_traded], trader)

        

eff_graph = Graph("efficiency")
trend_graph = Graph("efficiency trend")
pnl_graph = Graph("P&L")
volume_graph = Graph("volume")

def addToGraph(traders):
    for t in traders:
        e = efficiency(t)
        eff_graph.addTimeSerie(e)
        eff_graph.addTimeSerie(InstEfficiency(t))
        eff_graph.addTimeSerie(avg(e))
        trend_graph.addTimeSerie(trend(e))
        trend_graph.addTimeSerie(trend(InstEfficiency(t)))
        pnl_graph.addTimeSerie(PnL(t))
        volume_graph.addTimeSerie(VolumeTraded(t))

addToGraph([trader_150, trader_200, tf, 
            virtual_160, virtual_170, virtual_180, virtual_190, 
            tf_0_15, tf_0_015])

world.workTill(1500)

showGraphs("fv_trader", [price_graph, eff_graph, trend_graph, pnl_graph, volume_graph])
