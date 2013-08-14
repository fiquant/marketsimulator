from marketsim import request, combine, meta, types, _, registry, ops, context

from .. import _limit

import _meta 

class WithExpiry(_meta.OwnsSingleOrder):
    """ Limit-like order which is cancelled after given *delay*
    """
    
    def __init__(self, proto, delay):
        """ Initializes order with 'price' and 'volume'
        'limitOrderFactory' tells how to create limit orders
        """
        _meta.OwnsSingleOrder.__init__(self, proto)
        self._delay = delay
        
    def onOrderDisposed(self, order):
        self.owner.onOrderDisposed(self)
    
    def startProcessing(self):
        self.send(self.proto)
        self.world.scheduleAfter(self._delay, 
                                 _(self.orderBook, 
                                   request.Cancel(self.proto)).process)

class Factory(types.IOrderGenerator):
    
    def __init__(self, expiry , inner = _limit.Factory()):
        self.expiry = expiry
        self.inner = inner
        
    _properties = {
        'expiry': types.IFunction[float],
        'inner' : types.IOrderGenerator,  
    }

    def __call__(self):
        expiry = self.expiry()
        proto = self.inner()
        return WithExpiry(proto, expiry) \
            if expiry is not None and proto is not None else None 

LimitOrderFactorySignature = meta.function((types.Side,), meta.function((types.Price, types.Volume), types.IOrder))

@registry.expose(['WithExpiry'])
class WithExpiryFactory(object):
    """ Limit-like order which is cancelled after given *delay*
    """
    
    def __init__(self, expirationDistr=ops.constant(10)):
        self.expirationDistr = expirationDistr
        
    _types = [LimitOrderFactorySignature]
        
    _properties = {'expirationDistr'  : meta.function((), types.TimeInterval)}
    
    def create(self, side, price, volume):
        return WithExpiry(_limit.Limit(side, price, volume), 
                          self.expirationDistr())
    
    def __call__(self, side):
        return _(self, side).create
