from marketsim.veusz_graph import Graph, showGraphs
from marketsim.scheduler import Scheduler
from marketsim.order_queue import OrderBook
from marketsim.trader import SASM_Trader
from marketsim import Side
from marketsim.indicator import AssetPrice, OnEveryDt, ewma, dEWMA, EWMA, TraderEfficiency, \
    PnL, VolumeTraded, InstEfficiency
from marketsim.order import VirtualMarketOrderT
from marketsim import strategy

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

lp_A = strategy.LiquidityProvider(SASM_Trader(book_A), volumeDistr=lambda: 20)

trader_200 = SASM_Trader(book_A, "t200") 
trader_150 = SASM_Trader(book_A, "t150") 

strategy.FundamentalValue(trader_200, fundamentalValue=lambda: 200., volumeDistr=lambda: 5)
strategy.FundamentalValue(trader_150, fundamentalValue=lambda: 150., volumeDistr=lambda: 4)

def fv_virtual(fv):
    return strategy.FundamentalValue(SASM_Trader(book_A, "v"+str(fv)), 
                                     fundamentalValue=lambda: fv, 
                                     orderFactory=VirtualMarketOrderT, 
                                     volumeDistr=lambda: 1)

virtual_160 = fv_virtual(160.)
virtual_170 = fv_virtual(170.)
virtual_180 = fv_virtual(180.)
virtual_190 = fv_virtual(190.)

tf = strategy.TrendFollower(SASM_Trader(book_A, "TF"), average=ewma(0.015), volumeDistr=lambda: 5)

tf_0_15 = strategy.TrendFollower(SASM_Trader(book_A, "tf0.15"), orderFactory=VirtualMarketOrderT, average=ewma(0.15))
tf_0_015 = strategy.TrendFollower(SASM_Trader(book_A, "tf0.015"), orderFactory=VirtualMarketOrderT, average=ewma(0.015))

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
