from marketsim import parts, scheduler, order, _, mathutils, types, registry, ops, meta, observable
from .._generic import Generic
from marketsim.types import *

from .. import _wrap

class Noise(types.ISingleAssetStrategy):
    
    def getImpl(self):
        return Generic(self.orderFactory(parts.side.Random()), 
                       scheduler.Timer(self.creationIntervalDistr))
        
_wrap.strategy(Noise, ['Periodic', 'Noise'], 
                 """ Noise strategy is a quite dummy strategy that randomly creates an order 
                     and sends it to the order book. 
                     
                     It has following parameters:
    
                     |creationIntervalDistr| 
                         defines intervals of time between order creation 
                         (default: exponential distribution with |lambda| = 1)
                         
                     |volumeDistr| 
                         defines volumes of orders to create 
                         (default: exponential distribution with |lambda| = 1)
                 """,
                 [
                  ("orderFactory",  "order.factory.side.Market()",  'IFunction[Side] -> IOrderGenerator'),             
                  ("creationIntervalDistr", "mathutils.rnd.expovariate(1.)",'() -> TimeInterval'),
                 ], globals())
