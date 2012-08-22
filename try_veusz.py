from marketsim.veusz_graph import Graph
from marketsim.scheduler import world
from marketsim.order_queue import OrderBook
from marketsim.trader import LiquidityProvider
from marketsim import Side
from marketsim.indicator import AssetPrice, BidPrice, AskPrice, OnEveryDt
from marketsim.trader import EWMA_Ex

book_A = OrderBook(tickSize=0.01)
book_A.label = "A"

graph = Graph("arbitrage")
assetPrice = AssetPrice(book_A)
graph.addTimeSerie(assetPrice)
#graph.addTimeSerie(BidPrice(book_A))
#graph.addTimeSerie(AskPrice(book_A))

ewma_0_15 = EWMA_Ex(assetPrice, alpha=0.15)
ewma_0_015 = EWMA_Ex(assetPrice, alpha=0.015)
ewma_0_065 = EWMA_Ex(assetPrice, alpha=0.065)

graph.addTimeSerie(OnEveryDt(1, lambda: ewma_0_15.at(world.currentTime), "Avg(0.15)"))
graph.addTimeSerie(OnEveryDt(1, lambda: ewma_0_015.at(world.currentTime), "Avg(0.015)"))
graph.addTimeSerie(OnEveryDt(1, lambda: ewma_0_065.at(world.currentTime), "Avg(0.065)"))

seller_A = LiquidityProvider(book_A, Side.Sell)
buyer_A = LiquidityProvider(book_A, Side.Buy)

world.workTill(500)

graph.show()

world.reset()