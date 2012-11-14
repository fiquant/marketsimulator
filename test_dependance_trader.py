from marketsim import strategy, order, orderbook, trader


book_A = orderbook.Local()
book_B = orderbook.Local()

trader = strategy.Dependency(trader.SASM(book_A), book_B, factor=0.5, volumeDistr = lambda: 10).trader

for x in range(90,100):
    book_A.process(order.Limit.Buy(x, 1))
    
for x in range(101,110):
    book_A.process(order.Limit.Sell(x, 1))
    
assert book_A.asks.best.price == 101
assert book_A.bids.best.price == 99
assert book_A.price == 100
    
book_B.process(order.Limit.Sell(200, 10))
book_B.process(order.Limit.Buy(192, 10))
assert book_B.price == 196

assert book_A.asks.best.price == 101
assert book_A.bids.best.price == 97
assert book_A.price == 99

assert trader.amount == -2
assert trader.PnL == +99 +98

book_B.process(order.Limit.Buy(200,20))
book_B.process(order.Limit.Sell(208,20))
assert book_B.price == 204

assert book_A.asks.best.price == 103
assert book_A.bids.best.price == 97
assert book_A.price == 100

assert trader.amount == -2 +2
assert trader.PnL == +99 +98 -101 -102


