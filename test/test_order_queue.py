import sys
sys.path.append(r'..')

from marketsim import order
import test
from marketsim.orderbook._local import Asks

history = test.OrderQueueHistoryChecker()

asks = Asks()
asks.on_best_changed += history.append

a12 = order.Limit.Sell(12, 100)
a10 = order.Limit.Sell(10, 100)
a10_2 = order.Limit.Sell(10, 90)
a15 = order.Limit.Sell(15, 100)
asks.push(a12)
assert history.checkDelta([(12,100)])
asks.push(a10)
assert history.checkDelta([(10,100)])
asks.push(a15)
asks.push(a10_2)

assert asks.evaluateOrderPrice(10) == (10*10, 0)
assert asks.evaluateOrderPrice(110) == (110*10, 0)
assert asks.evaluateOrderPrice(200) == (190*10+10*12, 0)
assert asks.evaluateOrderPrice(300) == (190*10+100*12+10*15, 0)
assert asks.evaluateOrderPrice(400) == (190*10+100*12+100*15, 10)

S = [x.price for x in asks.sorted]
assert S == [10,10,12,15]

PVs = list(asks.sortedPVs)
assert PVs == [(10,190),(12,100),(15,100)]

L = set(asks.withPricesBetterThan(12))
assert a10 in L
assert a10_2 in L
assert a12 in L
assert a15 not in L
assert asks.volumeWithPriceBetterThan(9) == 0
assert asks.volumeWithPriceBetterThan(10) == 190
assert asks.volumeWithPriceBetterThan(11) == 190
assert asks.volumeWithPriceBetterThan(12) == 290
assert asks.volumeWithPriceBetterThan(15) == 390
assert asks.volumeWithPriceBetterThan(18) == 390

a10_2.cancel()

b = order.Limit.Buy(9, 100)
assert asks.matchWith(b) == False
assert b.volume == 100
assert b.PnL == 0
assert asks.best.price == 10
assert asks.best.volume == 100

b = order.Limit.Buy(10, 30)
assert asks.matchWith(b) == True
assert b.volume == 0
assert b.PnL == -10*30
assert asks.best.price == 10
assert asks.best.volume == 70
assert a10.PnL == +10*30
assert history.checkDelta([(10,70)])

b = order.Limit.Buy(10, 80)
assert asks.matchWith(b) == False
assert b.volume == 10
assert b.PnL == -10*70
assert asks.best.price == 12
assert asks.best.volume == 100
assert a10.PnL == +10*100
assert history.checkDelta([(12,100)])

b = order.Limit.Buy(20, 180)
assert asks.matchWith(b) == True
assert b.volume == 0
assert a12.PnL == +12*100
assert a15.PnL == +15*80
assert b.PnL == -12*100 -15*80
assert asks.best.price == 15
assert asks.best.volume == 20
assert history.checkDelta([(15,20)])

b = order.Limit.Buy(20, 180)
assert asks.matchWith(b) == False
assert b.volume == 160
assert b.PnL == -20*15
assert a15.PnL == +15*100
assert asks.empty
assert history.checkDelta([None])

