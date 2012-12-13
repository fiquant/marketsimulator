from marketsim import Event, Side, scheduler
from _base import Base
from _limit import Limit

class Cancel(object):
    """ Cancels another order that can be for example a limit or an iceberg order
    """
    def __init__(self, orderToBeCancelled):
        self._toCancel = orderToBeCancelled
        self.on_matched = Event() # just dummy event. never called
        self.on_charged = Event()
        
    def charge(self, price):
        self.on_charge.fire(price)
        
    def processIn(self, orderBook):
        orderBook.cancelOrder(self._toCancel)
        
    def clone(self):
        return Cancel(self._toCancel)
    
    def copyTo(self, dest):
        assert dest._toCancel == self._toCancel

class LimitMarket(Base):
    """ This a combination of a limit order and a cancel order sent immediately
    It works as a market order in sense that it is not put into the order queue 
    but can be matched (as a limit order) 
    only if there are orders with suitable price in the queue
    TBD: Cancelable order having delay and sched not None  
    """
    
    def __init__(self, side, price, volume, delay=None, sched=None):
        """ Initializes order with 'price' and 'volume'
        'limitOrderFactory' tells how to create limit orders
        """
        Base.__init__(self, side, volume)
        self._delay = delay
        # we create a limit order
        self._order = Limit(side, price, volume)
        # translate its events to our listeners
        self._order.on_matched += self.on_matched.fire
        self._scheduler = sched if sched else scheduler.current()
        
    def processIn(self, orderBook):
        orderBook.process(self._order)
        cancel = lambda: orderBook.process(Cancel(self._order))
         
        if self._delay is None: 
            cancel()
        else:
            self._scheduler.scheduleAfter(self._delay, cancel)
        
    @property 
    def volume(self):
        return self._order.volume 
    
    @property
    def PnL(self):
        return self._order.PnL
    
    @staticmethod
    def Buy(price, volume): return LimitMarket(Limit.Buy, price, volume)
    
    @staticmethod
    def Sell(price, volume): return LimitMarket(Limit.Sell, price, volume)
    
    @staticmethod
    def T(side): return lambda price, volume: LimitMarket(side, price, volume)
