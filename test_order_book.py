from marketsim import order
from marketsim.order_queue import *

book = OrderBook(tickSize=1)

a12 = order.Limit.Sell(11.2, 100)
book.processLimitOrder(a12)

assert book.asks.best == a12
assert book.bids.empty

b11 = order.Limit.Buy(11.9, 70)
book.processLimitOrder(b11)

assert book.bids.best == b11

a10 = order.Limit.Sell(9.9, 50)
book.processLimitOrder(a10)
assert a10.empty
assert a10.PnL == 11*50
assert book.bids.best.volume == 20
assert b11.PnL == -11*50

a9 = order.Limit.Sell(8.9, 50)
book.processLimitOrder(a9)
assert book.bids.empty
assert book.asks.best.price == 9
assert a9.volume == 30
assert a9.PnL == 11*20
assert b11.empty
assert b11.PnL == -11*70

mb_1 = order.Market.Buy(20)
assert book.processMarketOrder(mb_1)
assert mb_1.empty
assert mb_1.PnL == -20*9
assert a9.PnL == 220+20*9
assert a9.volume == 10

mb_2 = order.Market.Buy(120)
assert book.processMarketOrder(mb_2) == False
assert mb_2.volume == 10
assert mb_2.PnL == -9*10 - 12*100
assert a12.empty
assert a12.PnL == 12*100