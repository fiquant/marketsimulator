from marketsim import meta, types, _, registry, ops

from _limit import LimitFactory
from _cancel import Cancel
from _base import Base

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
    
    def __init__(self, expirationDistr=ops.constant(10), orderFactory = LimitFactory):
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
