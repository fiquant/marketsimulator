from marketsim import registry, request, context, event, _, combine, ops, types
from marketsim.types import *

from _meta import *


from marketsim.gen._intrinsic.order.meta.fixed_budget import Order_Impl as FixedBudget
from marketsim.gen._out.order._FixedBudget import FixedBudget as Factory


@registry.expose(['FixedBudget'])    
@sig((IFunction[Side],), IOrderGenerator)
class Side_Factory(object):
    
    def __init__(self, budget = ops.constant(200.)):
        self.budget = budget
        
    _properties = { 
        'budget'  : types.IFunction[float],
    }
    
    def __call__(self, side):
        return Factory(side, self.budget)
