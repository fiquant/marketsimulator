from marketsim import Side
from marketsim.order import *
from marketsim.order_queue import *
from marketsim.scheduler import Scheduler
from marketsim.test import *
from marketsim.trader import *
from marketsim.indicator import TraderEfficiency

world = Scheduler()

ask_history = OrderQueueHistoryChecker()
bid_history = OrderQueueHistoryChecker()

book = OrderBook(tickSize=.001)
book.asks.on_best_changed += ask_history.append
book.bids.on_best_changed += bid_history.append

trader = FVTrader(book, volumeDistr=(lambda:10), creationIntervalDistr=(lambda:1))
trader_efficiency = TraderEfficiency([trader.on_traded], trader)

fv_history = TraderHistoryChecker()
trader.on_traded += fv_history.append

world.workTill(1.5)

assert trader.PnL == 0
assert fv_history.checkDelta([])

book.process(LimitOrderSell(80, 10))
assert ask_history.checkDelta([(80,10)])
book.process(LimitOrderSell(90, 10))
book.process(LimitOrderSell(100, 10))

assert book.asks.best.price == 80
assert trader_efficiency.value == 0

world.workTill(2.5)

assert book.asks.best.price == 90
assert trader.PnL == -80*10
assert trader.amount == 10
assert trader_efficiency.value == None 
assert ask_history.checkDelta([(90,10)])
assert fv_history.checkDelta([(-800,10)])

world.workTill(3.5)

assert ask_history.checkDelta([(100,10)])
assert book.asks.best.price == 100
assert trader.PnL == -80*10 - 90*10
assert trader.amount == 10 + 10
assert fv_history.checkDelta([(-80*10 - 90*10, 10 + 10)])

world.workTill(4.5)

assert ask_history.checkDelta([])
assert book.asks.best.price == 100
assert trader.PnL == -80*10 - 90*10

book.process(LimitOrderBuy(110, 20))
assert bid_history.checkDelta([(110,10)])
assert ask_history.checkDelta([None])
assert book.asks.empty
assert book.bids.best.price == 110

world.workTill(5.5)

assert bid_history.checkDelta([None])
assert book.bids.empty
assert trader.PnL == -80*10 - 90*10 + 110*10
assert trader.amount == 10 + 10 - 10
assert fv_history.checkDelta([(-80*10 - 90*10 + 110*10, 10 + 10 - 10)])
