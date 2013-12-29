from marketsim import request, combine, meta, types, _, registry, bind, Side
from marketsim.types import *
from .. import _limit 

import _meta

from marketsim.gen._intrinsic.order.meta.ioc import Order_Impl as ImmediateOrCancel
from marketsim.gen._out.order._ImmediateOrCancel import ImmediateOrCancel as Factory
Order = ImmediateOrCancel

@registry.expose(['ImmediateOrCancel'])    
@meta.sig((IFunction[Side],), IOrderGenerator)
class Side_Factory(object):
    
    def __init__(self, 
                 factory = _limit.Side_Factory()):
        self.factory = factory
        
    _properties = {
        'factory' : meta.function((IFunction[Side],), IOrderGenerator)
    }
    
    def __call__(self, side):
        return Factory(self.factory(side))
