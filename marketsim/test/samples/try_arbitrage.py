from marketsim import trader, strategy, orderbook, remote, scheduler, observable, veusz

world = scheduler.create()

book_A = orderbook.Local(tickSize=0.01, label="A")
book_B = orderbook.Local(tickSize=0.01, label="B")

link = remote.TwoWayLink()
remote_A = orderbook.Remote(book_A, link)
remote_B = orderbook.Remote(book_B, link)

price_graph = veusz.Graph("Price")
spread_graph = veusz.Graph("Bid-Ask Spread")
cross_graph = veusz.Graph("Cross Bid-Ask Spread")

arbitrager = strategy.Arbitrage(\
   trader.SingleAssetMultipleMarket([remote_A, remote_B])).trader
 
assetPrice = observable.Price(book_A)

avg = observable.avg

cross_AB = observable.CrossSpread(book_A, book_B)
cross_BA = observable.CrossSpread(book_B, book_A)

cross_graph += [cross_AB,
                cross_BA,
                avg(cross_AB),
                avg(cross_BA)]

spread_graph += [avg(observable.BidPrice(book_A)),
                 avg(observable.AskPrice(book_A)),
                 avg(observable.BidPrice(book_B)),
                 avg(observable.AskPrice(book_B))]


ewma_0_15 = observable.EWMA(assetPrice, alpha=0.15)
ewma_0_015 = observable.EWMA(assetPrice, alpha=0.015)
ewma_0_065 = observable.EWMA(assetPrice, alpha=0.065)

price_graph += [assetPrice, 
                avg(assetPrice, 0.15),
                avg(assetPrice, 0.065),
                avg(assetPrice, 0.015)]

lp_A = strategy.LiquidityProvider(trader.SASM(remote_A))
lp_B = strategy.LiquidityProvider(trader.SASM(remote_B))

world.workTill(500)

veusz.render("arbitrage", [price_graph, spread_graph, cross_graph])
