from marketsim import Event, scheduler, registry, mathutils, types, meta, bind, Side, _
from _base import Base
from _limit import LimitFactory

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
    """
    
    def __init__(self, side, price, volume):
        """ Initializes order with 'price' and 'volume'
        'limitOrderFactory' tells how to create limit orders
        """
        Base.__init__(self, side, volume)
        # we create a limit order
        self._order = LimitFactory(side)(price, volume)
        # translate its events to our listeners
        self._order.on_matched += self.on_matched.fire
        
    def processIn(self, orderBook):
        orderBook.process(self._order)
        orderBook.process(Cancel(self._order))
        
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
    
@registry.expose(alias=['LimitMarket'])
@meta.sig(args=(Side,), rv=meta.function((types.Price,), types.IOrder))
def LimitMarketFactory(side):
    return bind.Construct(LimitMarket, side)

LimitMarketFactory.__doc__ = LimitMarket.__doc__

class WithExpiry(Base):
    """ Limit-like order which is cancelled after given *delay*
    """
    
    def __init__(self, order, delay, sched):
        """ Initializes order with 'price' and 'volume'
        'limitOrderFactory' tells how to create limit orders
        """
        Base.__init__(self, order.side, order.volume)
        self._delay = delay
        # we create a limit order
        self._order = order
        # translate its events to our listeners
        self._order.on_matched += self.on_matched.fire
        self._scheduler = sched
        
    def processIn(self, orderBook):
        orderBook.process(self._order)
        self._scheduler.scheduleAfter(self._delay, 
                                      _(orderBook, Cancel(self._order)).process)
        
    @property 
    def volume(self):
        return self._order.volume 
    
    @property
    def PnL(self):
        return self._order.PnL

LimitOrderFactorySignature = meta.function((types.Side,), meta.function((types.Price, types.Volume), types.IOrder))

@registry.expose(['WithExpiry'])
class WithExpiryFactory(object):
    """ Limit-like order which is cancelled after given *delay*
    """
    
    def __init__(self, expirationDistr=mathutils.constant(10), orderFactory = LimitFactory):
        self.expirationDistr = expirationDistr
        self.orderFactory = orderFactory
        
    def bind(self, context):
        self._scheduler = context.world
        
    _types = [LimitOrderFactorySignature]
        
    _properties = {'expirationDistr'  : meta.function((), types.TimeInterval),
                   'orderFactory' : LimitOrderFactorySignature}
    
    def create(self, side, price, volume):
        return WithExpiry(self.orderFactory(side)(price, volume), self.expirationDistr(), self._scheduler)
    
    def __call__(self, side):
        return _(self, side).create
