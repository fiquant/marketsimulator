from marketsim.order_queue import OrderBook
from marketsim.order import LimitOrderSell, LimitOrderBuy
from marketsim.scheduler import Scheduler
from marketsim.trader import SASM_Trader
from marketsim import strategy

world = Scheduler()
book = OrderBook()
trader = strategy.TrendFollower(SASM_Trader(book), creationIntervalDistr=lambda: 1, volumeDistr=lambda: 1)

for x in range(90, 100):
    book.process(LimitOrderBuy(x, 1))
    
for x in range(101, 111):
    book.process(LimitOrderSell(x, 1))
    
assert trader.amount == 0
assert trader.PnL == 0

world.workTill(0.9)

book.process(LimitOrderBuy(101,2))

assert book.asks.best.price == 102
assert book.price == 101.5

world.workTill(1.1)

assert book.asks.best.price == 103
assert book.price == 102

assert trader.amount == 1
assert trader.PnL == -102

book.process(LimitOrderSell(95,10))
assert book.asks.best.price == 95
assert book.bids.best.price == 94
    
world.workTill(2.1)

assert book.bids.best.price == 93
assert trader.amount == 0
assert trader.PnL == -102 +94
