from marketsim import request, combine, meta, types, _, registry, ops

import _limit

from _limit import Limit, LimitFactory
from _meta import OwnsSingleOrder

class WithExpiry(OwnsSingleOrder):
    """ Limit-like order which is cancelled after given *delay*
    """
    
    def __init__(self, proto, delay, sched):
        """ Initializes order with 'price' and 'volume'
        'limitOrderFactory' tells how to create limit orders
        """
        OwnsSingleOrder.__init__(self, proto)
        self._delay = delay
        # we create a limit order
        self._scheduler = sched
        
    def onOrderDisposed(self, order):
        self.owner.onOrderDisposed(self)
    
    def processIn(self, orderBook):
        self.orderBook = orderBook
        self.send(self.proto)
        self._scheduler.scheduleAfter(self._delay, 
                                      _(orderBook, request.Cancel(self.proto)).process)

class Factory(types.IOrderGenerator):
    
    def __init__(self, expiry , inner = _limit.Factory()):
        self.expiry = expiry
        self.inner = inner
        
    _properties = {
        'expiry': types.IFunction[float],
        'inner' : types.IOrderGenerator,  
    }

    def bind(self, ctx):
        self._scheduler = ctx.world
        
    def __call__(self):
        expiry = self.expiry()
        proto = self.inner()
        return WithExpiry(proto, expiry, self._scheduler) \
            if expiry is not None and proto is not None else None

LimitOrderFactorySignature = meta.function((types.Side,), meta.function((types.Price, types.Volume), types.IOrder))

@registry.expose(['WithExpiry'])
class WithExpiryFactory(object):
    """ Limit-like order which is cancelled after given *delay*
    """
    
    def __init__(self, expirationDistr=ops.constant(10)):
        self.expirationDistr = expirationDistr
        
    def bind(self, context):
        self._scheduler = context.world
        
    _types = [LimitOrderFactorySignature]
        
    _properties = {'expirationDistr'  : meta.function((), types.TimeInterval)}
    
    def create(self, side, price, volume):
        return WithExpiry(Limit(side, price, volume), 
                          self.expirationDistr(), 
                          self._scheduler)
    
    def __call__(self, side):
        return _(self, side).create
