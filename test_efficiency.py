from marketsim.trader import SingleAssetTrader
from marketsim.order_queue import OrderBook
from marketsim.indicator import TraderEfficiency
from marketsim.order import LimitOrderBuy, LimitOrderSell, MarketOrderBuy, MarketOrderSell

book = OrderBook()

book.process(LimitOrderBuy(90, 10))
book.process(LimitOrderSell(110, 10))

class Trader(SingleAssetTrader):
    
    def __init__(self, book):
        SingleAssetTrader.__init__(self)
        self.book = book
        self.efficiency = TraderEfficiency([self.on_traded], self)
        
    def buy(self, volume):
        self.send(self.book, MarketOrderBuy(volume))
        
    def sell(self, volume):
        self.send(self.book, MarketOrderSell(volume))
        
trader = Trader(book)

assert trader.efficiency.value == 0

trader.buy(3)

assert trader.PnL == -3*110
assert trader.amount == 3
assert trader.efficiency.value == -3*110 + 3*90

trader.sell(5)

assert trader.PnL == -3*110 + 5*90
assert trader.amount == -2
assert trader.efficiency.value == -3*110 + 5*90 - 2*110

######## ----------------------  testing trader efficiency with remote book      

from marketsim.scheduler import Scheduler
from marketsim.remote_book import TwoWayLink, RemoteBook

world = Scheduler()

link = TwoWayLink(latencyUp=lambda: 1, latencyDown=lambda: 1)
rbook = RemoteBook(book, link)
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