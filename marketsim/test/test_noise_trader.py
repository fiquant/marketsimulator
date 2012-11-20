from marketsim import strategy, order, orderbook, trader, Side, scheduler

world = scheduler.create()

book = orderbook.Local(tickSize=.001)

counter = [0]

def side():
    counter[0] = 1 - counter[0]
    return Side.byId(counter[0])

trader = strategy.Noise(trader.SASM(book), sideDistr=side, volumeDistr=(lambda:10), creationIntervalDistr=(lambda:1)).trader

world.workTill(1.5)

book.process(order.Limit.Buy(90, 20))
book.process(order.Limit.Sell(110, 20))

world.workTill(2.5)

assert book.bids.best.volume == 10
assert trader.PnL == +10*90

world.workTill(3.5)

assert book.asks.best.volume == 10
assert trader.PnL == +10*90 - 10*110