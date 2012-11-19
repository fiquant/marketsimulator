from marketsim import signal, strategy, order, orderbook, trader, scheduler

world = scheduler.create()

book = orderbook.Local(tickSize=.001)

signal = signal.RandomWalk(initialValue=-2, deltaDistr=(lambda: 1), intervalDistr=(lambda:1))

trader = strategy.Signal(trader.SASM(book), signal, volumeDistr=(lambda:10)).trader

book.process(order.Limit.Sell(110,10))
book.process(order.Limit.Sell(120,10))

book.process(order.Limit.Buy(80,10))
book.process(order.Limit.Buy(90,10))

assert book.bids.best.price == 90

world.workTill(1.5)

assert book.bids.best.price == 80
assert trader.PnL == 90*10

world.workTill(2.5)

assert book.bids.best.price == 80
assert book.asks.best.price == 110
assert trader.PnL == 90*10

world.workTill(3.5)

assert book.bids.best.price == 80
assert book.asks.best.price == 120
assert trader.PnL == 90*10 - 110*10

world.workTill(4.5)

assert book.bids.best.price == 80
assert book.asks.empty
assert trader.PnL == 90*10 - 110*10 - 120*10
