from .. import _limit 
import _meta 
from marketsim import context, ops, request, meta, types, registry, bind, event, _, combine

from marketsim.types import *

class Iceberg(_meta.OwnsSingleOrder):
    """ Virtual order that implements iceberg strategy:
    First it sends an order for a small potion of its volume to a book and
    once it is filled resends a new order 
    """

    def __init__(self, lotSize, proto):
        """ Initializes iceberg order
        lotSize -- maximal volume for order that can be sent
        orderFactory -- factory to create real orders: *args -> Order
        *args -- parameters to be passed to real orders
        """
        _meta.OwnsSingleOrder.__init__(self, proto)
        self._lotSize = lotSize
        
    def With(self, **kwargs):
        return Iceberg(self._lotSize, self.proto.With(**kwargs))
                
    def onOrderDisposed(self, order):
        if not self.cancelled:
            self._tryToResend()
        _meta.OwnsSingleOrder.onOrderDisposed(self, order)
            
    def _tryToResend(self):
        """ Tries to send a real order to the order book
        """
        self.send(self.proto.With(volume = min(self._lotSize, self.volumeUnmatched)))

    def startProcessing(self):
        """ Called when an order book tries to determine 
        how the order should be processed 
        """
        self._tryToResend()
        
class Factory(IOrderGenerator):
    
    def __init__(self, 
                 lotSize = ops.constant(1), 
                 factory = _limit.Factory()):
        self.lotSize = lotSize
        self.factory = factory
        
    _properties = {
        'lotSize' : IFunction[float],
        'factory' : IOrderGenerator
    }
    
    def __call__(self):
        lotSize = self.lotSize()
        if lotSize is None:
            return None
        proto = self.factory()
        if proto is None:
            return None
        order = Iceberg(lotSize, proto)
        return order

@registry.expose(['Iceberg'])    
@sig((IFunction[Side],IFunction[float]), IOrderGenerator)
class SidePrice_Factory(object):
    
    def __init__(self, 
                 lotSize = ops.constant(1), 
                 factory = _limit.SidePrice_Factory()):
        self.lotSize = lotSize
        self.factory = factory
        
    _properties = {
        'lotSize' : IFunction[float],
        'factory' : function((IFunction[Side],IFunction[float]), IOrderGenerator)
    }
    
    def __call__(self, side, price):
        return Factory(self.lotSize, self.factory(side, price))

@registry.expose(['Iceberg'])    
@sig((IFunction[Side],), IOrderGenerator)
class Side_Factory(object):
    
    def __init__(self, 
                 lotSize = ops.constant(1), 
                 factory = _limit.Side_Factory()):
        self.lotSize = lotSize
        self.factory = factory
        
    _properties = {
        'lotSize' : IFunction[float],
        'factory' : meta.function((IFunction[Side],), IOrderGenerator)
    }
    
    def __call__(self, side):
        return Factory(self.lotSize, self.factory(side))
    
@registry.expose(['Iceberg'])    
class Side_Price_Factory(IFunction[IFunction[IOrderGenerator, 
                                       IFunction[float]], 
                             IFunction[Side]]):
    
    def __init__(self, 
                 lotSize = ops.constant(1), 
                 factory = _limit.Side_Price_Factory()):
        self.lotSize = lotSize
        self.factory = factory
        
    _properties = {
        'lotSize' : IFunction[float],
        'factory' : IFunction[IFunction[IOrderGenerator, 
                                        IFunction[float]], 
                              IFunction[Side]]
    }
    
    def __call__(self, side):
        return Price_Factory(self.lotSize, self.factory(side))
    
class Price_Factory(IFunction[IOrderGenerator, IFunction[float]]):
    
    def __init__(self, 
                 lotSize = ops.constant(1), 
                 factory = _limit.Price_Factory()):
        self.lotSize = lotSize
        self.factory = factory
        
    _properties = {
        'lotSize' : IFunction[float],
        'factory' : IFunction[IOrderGenerator, IFunction[float]]
    }
    
    def __call__(self, price):
        return Factory(self.lotSize, self.factory(price))
