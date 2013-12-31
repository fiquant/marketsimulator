from marketsim import ops, Side, types, combine, registry, context, bind, observable, event, meta, _
from .. import _market, _limit
import _meta

from marketsim.types import *

from marketsim.gen._intrinsic.order.meta.stoploss import Order_Impl as StopLoss
from marketsim.gen._out.order._StopLoss import (StopLoss as Factory, side_StopLoss as Side_Factory)

@registry.expose(['Stoploss'])
@sig((IFunction[Side],IFunction[float]), IOrderGenerator)
class SidePrice_Factory(object):
    
    def __init__(self, 
                 maxloss = ops.constant(0.1), 
                 factory = _limit.SidePrice_Factory()):
        self.maxloss = maxloss
        self.factory = factory
        
    _properties = {
        'maxloss':  IFunction[float],
        'factory' : function((IFunction[Side],IFunction[float]), IOrderGenerator)
    }
    
    def __call__(self, side, price):
        return Factory(self.maxloss, self.factory(side, price))
