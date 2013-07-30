from marketsim import parts, scheduler, order, _, mathutils, types, registry, ops, meta, observable
from _periodic import Generic
from marketsim.types import *

import _wrap

class Noise(types.ISingleAssetStrategy):
    
    def getDefinitions(self):
        return { 'side' : parts.side.Random() }
    
    def getImpl(self):
        return Generic(eventGen = scheduler.Timer(self.creationIntervalDistr), 
                       orderFactory = order.factory.Market(_.side, self.volumeDistr))
        
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
                  ("volumeDistr",           "mathutils.rnd.expovariate(1.)",'() -> Volume'),
                  ("creationIntervalDistr", "mathutils.rnd.expovariate(1.)",'() -> TimeInterval')
                 ], globals())
