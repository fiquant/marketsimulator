from marketsim import Side, order, orderbook

book = orderbook.Local(tickSize = 1)

book.process(order.Limit.Sell(100,10))

ab = order.AlwaysBest(10, side = Side.Sell)

book.process(ab)

assert book.asks.best.price == 99
assert ab.volume == 10
assert ab.PnL == 0

book.process(order.Limit.Sell(98,10))

assert book.asks.best.price == 97
assert ab.volume == 10
assert ab.PnL == 0

book.process(order.Limit.Buy(98,5))

assert book.asks.best.price == 97
assert ab.volume == 5
assert ab.PnL == +97*5

book.process(order.Limit.Buy(98,10))

assert book.asks.best.price == 98
assert ab.volume == 0
assert ab.PnL == +97*10

