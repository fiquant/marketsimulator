from marketsim.veusz_graph import Graph, showGraphs
from marketsim.scheduler import world
from marketsim.order_queue import OrderBook
from marketsim.trader import LiquidityProvider, FVTrader
from marketsim.arbitrage_trader import ArbitrageTrader
from marketsim import Side
from marketsim.indicator import AssetPrice, BidPrice, AskPrice, OnEveryDt, EWMA, CrossSpread

book_A = OrderBook(tickSize=0.01, label="A")
book_B = OrderBook(tickSize=0.01, label="B")

price_graph = Graph("Price")
spread_graph = Graph("Bid-Ask Spread")
cross_graph = Graph("Cross Bid-Ask Spread")

arbitrager = ArbitrageTrader(book_A, book_B)
 
assetPrice = AssetPrice(book_A)
price_graph.addTimeSerie(assetPrice)

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha=0.15))

cross_AB = CrossSpread(book_A, book_B)
cross_BA = CrossSpread(book_B, book_A)
cross_graph.addTimeSerie(cross_AB)
cross_graph.addTimeSerie(cross_BA)

spread_graph.addTimeSerie(avg(BidPrice(book_A)))
spread_graph.addTimeSerie(avg(AskPrice(book_A)))

spread_graph.addTimeSerie(avg(BidPrice(book_B)))
spread_graph.addTimeSerie(avg(AskPrice(book_B)))


ewma_0_15 = EWMA(assetPrice, alpha=0.15)
ewma_0_015 = EWMA(assetPrice, alpha=0.015)
ewma_0_065 = EWMA(assetPrice, alpha=0.065)

price_graph.addTimeSerie(OnEveryDt(1, ewma_0_15))
price_graph.addTimeSerie(OnEveryDt(1, ewma_0_015), {r'PlotLine/bezierJoin':True})
price_graph.addTimeSerie(OnEveryDt(1, ewma_0_065))

seller_A = LiquidityProvider(book_A, Side.Sell)
buyer_A = LiquidityProvider(book_A, Side.Buy)

seller_B = LiquidityProvider(book_B, Side.Sell)
buyer_B = LiquidityProvider(book_B, Side.Buy)

world.workTill(500)

showGraphs("arbitrage", [price_graph, spread_graph, cross_graph])

world.reset()