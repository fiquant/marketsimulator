from marketsim.veusz_graph import Graph, showGraphs
from marketsim.scheduler import Scheduler
from marketsim.order_queue import OrderBook
from marketsim.trader import LiquidityProvider, FVTrader
from marketsim import Side
from marketsim.indicator import AssetPrice, OnEveryDt, EWMA, TraderEfficiency, PnL

world = Scheduler()

book_A = OrderBook(tickSize=0.01, label="A")

price_graph = Graph("Price")
 
assetPrice = AssetPrice(book_A)
price_graph.addTimeSerie(assetPrice)

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

price_graph.addTimeSerie(avg(assetPrice))

seller_A = LiquidityProvider(book_A, Side.Sell)
buyer_A = LiquidityProvider(book_A, Side.Buy)
trader = FVTrader(book_A, fundamentalValue=lambda: 200.)

trader.label = "fv"
trader.efficiency = TraderEfficiency([trader.on_traded], trader)

eff_graph = Graph("efficiency")
eff_graph.addTimeSerie(trader.efficiency)
eff_graph.addTimeSerie(PnL(trader))

world.workTill(500)

showGraphs("fv_trader", [price_graph, eff_graph])
