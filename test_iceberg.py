from marketsim.order import *
from marketsim.iceberg import *
from marketsim.order_queue import *
from marketsim.test import *

book = OrderBook(tickSize=1)

createLimitSell = iceberg(10, LimitOrderSell)

a12 = createLimitSell(11.2, 100)
book.process(a12)

assert book.asks.best.price == 12
assert book.asks.best.volume == 10

assert a12.PnL == 0
assert a12.volume == 100
assert a12.price == 11.2  # price correction is done only for real options

assert book.bids.empty

mb1 = MarketOrderBuy(25)
book.process(mb1)

assert a12.PnL == 12*25
assert a12.volume == 75
assert mb1.empty
assert mb1.PnL == -12*25
assert book.asks.best.price == 12
assert book.asks.best.volume == 5

createMarketBuy = iceberg(25, MarketOrderBuy)
mb2 = createMarketBuy(65)
book.process(mb2)
assert a12.PnL == 12*90
assert a12.volume == 10
assert mb2.empty
assert mb2.PnL == -12*65

a12.cancel()
assert a12.cancelled
assert book.asks.empty

