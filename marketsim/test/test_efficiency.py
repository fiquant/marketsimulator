from marketsim import order, orderbook, remote, trader, observable

book = orderbook.Local()

book.process(order.Limit.Buy(90, 10))
book.process(order.Limit.Sell(110, 10))

class Trader(trader.SingleAsset):
    
    def __init__(self, book):
        trader.SingleAsset.__init__(self)
        self.book = book
        self.efficiency = observable.Efficiency(self)
        
    def buy(self, volume):
        self.send(self.book, order.Market.Buy(volume))
        
    def sell(self, volume):
        self.send(self.book, order.Market.Sell(volume))
        
ltrader = Trader(book)

assert ltrader.efficiency.value == 0

ltrader.buy(3)

assert ltrader.PnL == -3*110
assert ltrader.amount == 3
assert ltrader.efficiency.value == -3*110 + 3*90

ltrader.sell(5)

assert ltrader.PnL == -3*110 + 5*90
assert ltrader.amount == -2
assert ltrader.efficiency.value == -3*110 + 5*90 - 2*110

######## ----------------------  testing trader efficiency with remote book      

from marketsim.scheduler import Scheduler

world = Scheduler()

link = remote.TwoWayLink(latencyUp=lambda: 1, latencyDown=lambda: 1)
rbook = orderbook.Remote(book, link)
rtrader = Trader(rbook) 

assert rtrader.efficiency.value == None

rtrader.buy(3)
assert rtrader.PnL == 0
assert rtrader.amount == 0
assert rtrader.efficiency.value == None

world.workTill(2.5)

assert rtrader.PnL == -3*110
assert rtrader.amount == 3
assert rtrader.efficiency.value == 0

world.workTill(4.5)

assert rtrader.efficiency.value == -3*110 + 3*90

rtrader.sell(5)

world.workTill(7)

assert rtrader.PnL == -3*110 + 5*90
assert rtrader.amount == 3-5
assert rtrader.efficiency.value == -3*110 + 3*90

world.workTill(9)

assert rtrader.efficiency.value == -3*110 + 5*90 -2*110 