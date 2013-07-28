from marketsim import types, Side, ops, context, combine
from marketsim.types import *

from _market import Market as MarketOrder

def correct_volume(x):
    return None if x is None or abs(x) < 1 else int(x)
    
def correct_price(x):
    return x
    
def correct_budget(x):
    return x
    
def correct_side(x):
    return x

class Market_Base(types.IOrderGenerator):
    
    def __call__(self):
        params = self.get()
        return MarketOrder(*params) if params is not None else None

class Market(Market_Base, combine.SideVolume):
    
    def get(self):
        return combine.SideVolume.__call__(self)
    
class MarketSigned(Market_Base, combine.SignedVolume):
    
    def get(self):
        return combine.SignedVolume.__call__(self)

class SignedVolume_Market(IFunction[IOrderGenerator, SignedVolume]):
    
    def __call__(self, signedVolume):
        return MarketSigned(signedVolume)
    
class Side_Market(IFunction[IOrderGenerator, Side]):
    
    def __init__(self, 
                 volume = ops.constant(1.)):
        self.volume = volume
        
    _properties = { 
        'volume'    : types.IFunction[float]
    }
        
    def __call__(self, side):
        return Market(side, self.volume)

from _limit import Limit as LimitOrder, LimitOrderFactory
    
class Limit(types.IOrderGenerator, combine.SidePriceVolume):
    
    def __call__(self):
        params = combine.SidePriceVolume.__call__(self)
        return LimitOrder(*params) if params is not None else None
    
limit = {}

limit[types.SidePriceVolume] = Construct[IOrder, SidePriceVolume](LimitOrder)   
    
class SidePrice_Limit(IFunction[IOrderGenerator, SidePrice]):
    
    def __init__(self, volume = ops.constant(1.)):
        self.volume = volume
        
    _properties = { 'volume' : types.IFunction[float] }
    
    def __call__(self, side, price):
        return Limit(side, price, self.volume)
    
class Side_Limit(IFunction[IOrderGenerator, Side]):
    
    def __init__(self, price = ops.constant(100.), volume = ops.constant(1.)):
        self.price = price
        self.volume = volume
        
    _properties = { 
        'price'  : types.IFunction[float],
        'volume' : types.IFunction[float] 
    }
    
    def __call__(self, side):
        return Limit(side, self.price, self.volume)
    
from _fixed_budget import FixedBudget as FixedBudgetOrder

class FixedBudget(types.IOrderGenerator, combine.SideBudget):
    
    def __call__(self):
        params = combine.SideBudget.__call__(self)
        return FixedBudgetOrder(*params) if params is not None else None

class Side_FixedBudget(IFunction[IOrderGenerator, Side]):
    
    def __init__(self, budget = ops.constant(200.)):
        self.budget = budget
        
    _properties = { 
        'budget' : types.IFunction[float],
    }
    
    def __call__(self, side):
        return FixedBudget(side, self.budget)
    
from _always_best import AlwaysBest2 as AlwaysBestOrder

class AlwaysBestLimit(types.IOrderGenerator):
    
    def __init__(self, 
                 side = ops.constant(Side.Sell), 
                 volume = ops.constant(1.)):
        self.side = side
        self.volume = volume
        
    _properties = { 
        'side'      : types.IFunction[Side],
        'volume'    : types.IFunction[float],
    }
    
    def bind(self, ctx):
        self._ctx = ctx.context.copy()
        
    def __call__(self):
        side = correct_side(self.side())
        if side is None:
            return None
        volume = correct_volume(self.volume())
        if volume is None:
            return None
        order = AlwaysBestOrder(side, volume)
        context.bind(order, self._ctx)
        return order

class Side_AlwaysBestLimit(IFunction[IOrderGenerator, Side]):
    
    def __init__(self, volume = ops.constant(1.)):
        self.volume = volume
        
    _properties = { 
        'volume' : types.IFunction[float],
    }
    
    def __call__(self, side):
        return AlwaysBestLimit(side, self.volume)
    
