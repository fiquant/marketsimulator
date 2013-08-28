from marketsim import registry, context, request, _, event, Event, types, ops
from marketsim.types import *

import _meta
from .. import _limit

class FloatingPrice(_meta.OwnsSingleOrder): 
    """ Meta order controlling price of the underlying order
        When price changes it cancels underlying order and resends it with changed price
        For the moment we work only on limit orders but this mecanism might be extented to any persistent order
    """
    
    def __init__(self, proto, price):
        _meta.OwnsSingleOrder.__init__(self, proto)
        self._priceFunc = price
        event.subscribe(price, _(self)._update, self)
        
    def With(self, **kwargs):
        return FloatingPrice(self.proto.With(**kwargs), self._priceFunc)
    
    def cancel(self):
        _meta.OwnsSingleOrder.cancel(self)
        
    def startProcessing(self):
        self._update(None)
        
    def _update(self, dummy):
        if self.active:
            self._dispose() 
            price = self._priceFunc()
            if price is not None:
                self.send(self.proto.With(price = price, 
                                          volume = self.volumeUnmatched))
            else:
                self.send(None)

class Factory(types.IPersistentOrderGenerator):
    
    def __init__(self, 
                 price = ops.constant(100), 
                 factory = _limit.Price_Factory()):
        self.price = price 
        self.factory = factory
        
    _properties = { # IPersistentOrderFactory[Price]
        'price'   : types.IObservable[float],
        'factory' : types.IFunction[IOrderGenerator, IFunction[float]] 
    }
    
    def __call__(self):
        proto = self.factory(ops.constant(self.price()))()
        return FloatingPrice(proto, self.price) if proto is not None else None

@registry.expose(['Floating price'])
@sig((IFunction[Side],), IOrderGenerator)
class Side_Factory(object):
    
    def __init__(self, 
                 price = ops.constant(100), 
                 factory = _limit.Side_Price_Factory()):
        self.price = price 
        self.factory = factory
        
    _properties = { # IPersistentOrderFactory[Price]
        'price'   : IObservable[float],
        'factory' : IFunction[IFunction[IOrderGenerator, 
                                        IFunction[float]], 
                              IFunction[Side]] 
    }
    
    def __call__(self, side):
        return Factory(self.price, self.factory(side))
    