from marketsim import request, combine, meta, types, _, registry, ops

import _limit

from _limit import Limit, LimitFactory
from _meta import OwnsSingleOrder

class WithExpiry(OwnsSingleOrder):
    """ Limit-like order which is cancelled after given *delay*
    """
    
    def __init__(self, orderGenerator, delay, sched):
        """ Initializes order with 'price' and 'volume'
        'limitOrderFactory' tells how to create limit orders
        """
        self._orderGenerator = orderGenerator
        self._delay = delay
        # we create a limit order
        self._scheduler = sched
        
    def onOrderDisposed(self, order):
        self.owner.onOrderDisposed(self)
    
    def processIn(self, orderBook):
        order = self._orderGenerator()
        if order is not None:
            # this initialization should be done in processIn
            OwnsSingleOrder.__init__(self, order.side, order.volumeUnmatched, None, order.volumeFilled)
            self.orderBook = orderBook
            self.send(order)
            self._scheduler.scheduleAfter(self._delay, 
                                          _(orderBook, request.Cancel(self.order)).process)

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
        return WithExpiry(self.inner, expiry, self._scheduler)

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
    
    def _createInnerOrder(self):
        return Limit(*self._params)
    
    def create(self, side, price, volume):
        self._params = (side, price, volume)
        return WithExpiry(_(self)._createInnerOrder, self.expirationDistr(), self._scheduler)
    
    def __call__(self, side):
        return _(self, side).create
