from marketsim import request, combine, meta, types, _, registry, ops

import _limit

from _limit import Limit, LimitFactory
from _base import MetaBase

class WithExpiry(MetaBase):
    """ Limit-like order which is cancelled after given *delay*
    """
    
    def __init__(self, order, delay, sched):
        """ Initializes order with 'price' and 'volume'
        'limitOrderFactory' tells how to create limit orders
        """
        MetaBase.__init__(self, order.side, order.volume)
        self._delay = delay
        # we create a limit order
        self._order = order
        order.owner = self
        self._scheduler = sched
        
    def _onOrderCancelled(self, order):
        self.owner._onOrderCancelled(self)
    
    def processIn(self, orderBook):
        orderBook.process(self._order)
        self._scheduler.scheduleAfter(self._delay, 
                                      _(orderBook, request.Cancel(self._order)).process)
        
    @property 
    def volume(self):
        return self._order.volume 
    
    @property
    def PnL(self):
        return self._order.PnL

class Factory(types.IOrderGenerator):
    
    def __init__(self, expiry , inner = _limit.Factory):
        self.expiry = expiry
        self.inner = inner
        
    _properties = {
        'expiry': types.IFunction[float],
        'inner' : types.IPersistentOrderGenerator,  
    }

    def bind(self, ctx):
        self._scheduler = ctx.world
        
    def __call__(self):
        expiry = self.expiry()
        order = self.inner()
        return WithExpiry(order, expiry, self._scheduler) \
                  if order is not None and expiry is not None else \
               None

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
