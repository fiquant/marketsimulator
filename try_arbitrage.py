from marketsim.veusz_graph import Graph, showGraphs
from marketsim.scheduler import Scheduler
from marketsim import trader, strategy, orderbook, remote
from marketsim.indicator import AssetPrice, BidPrice, AskPrice, OnEveryDt, EWMA, CrossSpread


world = Scheduler()

book_A = orderbook.Local(tickSize=0.01, label="A")
book_B = orderbook.Local(tickSize=0.01, label="B")

link = remote.TwoWayLink()
remote_A = orderbook.Remote(book_A, link)
remote_B = orderbook.Remote(book_B, link)

price_graph = Graph("Price")
spread_graph = Graph("Bid-Ask Spread")
cross_graph = Graph("Cross Bid-Ask Spread")

arbitrager = strategy.Arbitrage(trader.SingleAssetMultipleMarket([remote_A, remote_B]))
 
assetPrice = AssetPrice(book_A)
price_graph.addTimeSerie(assetPrice)

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

cross_AB = CrossSpread(book_A, book_B)
cross_BA = CrossSpread(book_B, book_A)
cross_graph.addTimeSerie(cross_AB)
cross_graph.addTimeSerie(cross_BA)
cross_graph.addTimeSerie(avg(cross_AB))
cross_graph.addTimeSerie(avg(cross_BA))

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

lp_A = strategy.LiquidityProvider(trader.SASM(remote_A))
lp_B = strategy.LiquidityProvider(trader.SASM(remote_B))

world.workTill(500)

showGraphs("arbitrage", [price_graph, spread_graph, cross_graph])
