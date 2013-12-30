from _base import *
from marketsim import combine, registry, bind, ops, meta, types
from marketsim.types import *

from marketsim.gen._intrinsic.order.limit import Order_Impl as Limit
from marketsim.gen._out.order._Limit import (Limit as Factory, Side_Limit as Side_Factory)

Order = Limit

@registry.expose(['Limit'])
@sig((IFunction[Side],IFunction[float]), IOrderGenerator)
class SidePrice_Factory(combine.Volume):
    
    def __call__(self, side, price):
        return Factory(side, price, self.volume)
    
class Price_Factory(IFunction[IOrderGenerator, IFunction[float]]):
    
    def __init__(self, 
                 side = ops.constant(Side.Sell), 
                 volume = ops.constant(1.)):
        self.side = side
        self.volume = volume
        
    _properties = { 
        'side'   : types.IFunction[Side],
        'volume' : types.IFunction[float],
     }
    
    def __call__(self, price):
        return Factory(self.side, price, self.volume)
    
@registry.expose(['Limit'])    
class Side_Price_Factory(IFunction[IFunction[IOrderGenerator, 
                                             IFunction[float]], 
                                   IFunction[Side]]):
    
    def __init__(self, 
                 volume = ops.constant(1.)):
        self.volume = volume
        
    _properties = { 
        'volume' : types.IFunction[float],
     }
    
    def __call__(self, side):
        return Price_Factory(side, self.volume)

class PriceVolume_Factory(IFunction[IOrderGenerator, PriceVolume]):
    
    def __init__(self, side = ops.constant(Side.Sell)):
        self.side = side
        
    _properties = { 
        'side'   : types.IFunction[Side]
     }
    
    def __call__(self, price, volume):
        return Factory(self.side, price, volume)

class Volume_Factory(IFunction[IOrderGenerator, PriceVolume]):
    
    def __init__(self, 
                 side = ops.constant(Side.Sell),
                 price = ops.constant(100.)):
        self.side = side
        self.price = price
        
    _properties = { 
        'side'   : types.IFunction[Side],
        'price'  : types.IFunction[float],
     }
    
    def __call__(self, volume):
        return Factory(self.side, self.price, volume)

    
class LimitOrderFactory(types.IFunction[types.IOrder, types.SidePriceVolume]):
    
    def __call__(self, side, price, volume):
        return Order(side, price, volume)
    
@registry.expose(alias=['Limit'])
@sig(args=(Side,), rv=function((Price, Volume,), IOrder))
def LimitFactory(side):
    return bind.Construct(Order, side)

LimitFactory.__doc__ = Order.__doc__

class AdaptLimit_SidePriceBound(object):
    
    def __init__(self, orderFactory, side, price):
        self.orderFactory = orderFactory
        self.side = side
        self.price = price
        
    def __call__(self, volume):
        return self.orderFactory(self.side)(self.price, volume)

@registry.expose(alias=['Adapt limit order'])
class AdaptLimit(object):
    """ Adapts limit-like orders for usage where market-like orders are expected.
    User should provide *priceFunc* calculating price of order to create
    """
    
    def __init__(self, orderFactory = LimitFactory, priceFunc = ops.constant(100)):
        self.orderFactory = orderFactory
        self.priceFunc = priceFunc
        
    _properties = { 'orderFactory' : meta.function(args=(Side,), rv=function((Price, Volume,), IOrder)),
                    'priceFunc'    : meta.function((), Price)}
    
    _types = [meta.function(args=(Side,), rv=function((Volume,), IOrder))]
    
    def __repr__(self):
        return 'AdaptLimit(' + repr(self.orderFactory) + ', ' + repr(self.priceFunc) + ')'
        
    def __call__(self, side):
        price = self.priceFunc()
        price = self.priceFunc()
        return AdaptLimit_SidePriceBound(self.orderFactory, side, price)
