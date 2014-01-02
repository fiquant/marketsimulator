from .. import _limit 
import _meta 
from marketsim import context, ops, request, meta, types, registry, bind, event, _, combine

from marketsim.types import *

from marketsim.gen._out.order._Iceberg import (Iceberg as Factory,
                                               sideprice_Iceberg as SidePrice_Factory,
                                               side_Iceberg as Side_Factory,
                                               price_Iceberg as Price_Factory)

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
