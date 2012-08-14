from marketsim import Side
from marketsim.scheduler import world
from marketsim.order import *
from marketsim.order_queue import *
from marketsim.trader import *

book = OrderBook(tickSize=.001)


trader = FVTrader(book, volumeDistr=(lambda:10), creationIntervalDistr=(lambda:1))

world.workTill(1.5)

assert trader.PnL == 0

book.process(LimitOrderSell(80, 10))
book.process(LimitOrderSell(90, 10))
book.process(LimitOrderSell(100, 10))

assert book.asks.best.price == 80

world.workTill(2.5)

assert book.asks.best.price == 90
assert trader.PnL == -80*10

world.workTill(3.5)

assert book.asks.best.price == 100
assert trader.PnL == -80*10 - 90*10

world.workTill(4.5)

assert book.asks.best.price == 100
assert trader.PnL == -80*10 - 90*10

book.process(LimitOrderBuy(110, 20))
assert book.asks.empty
assert book.bids.best.price == 110

world.workTill(5.5)

assert book.bids.empty
assert trader.PnL == -80*10 - 90*10 + 110*10