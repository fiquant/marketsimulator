from marketsim.types import *
from marketsim import (orderbook, observable, scheduler, order, mathutils, types, meta, 
                       registry, bind, defs, _, parts)

from .. import _wrap
from .._generic import Generic

class TwoAverages(types.ISingleAssetStrategy):

    def getImpl(self):
        return  Generic(self.orderFactory(
                            parts.side.TwoAverages(
                                            self.ewma_alpha1, 
                                            self.ewma_alpha2, 
                                            self.threshold)),
                        scheduler.Timer(self.creationIntervalDistr))

_wrap.strategy(TwoAverages, ['Periodic', 'TwoAverages'], 
             """ Two averages strategy compares two averages of price of the same asset but
                 with different parameters ('slow' and 'fast' averages) and when 
                 the first is greater than the second one it buys, 
                 when the first is lower than the second one it sells
                 
                 It has following parameters:

                 |ewma_alpha1| 
                     parameter |alpha| for the first exponentially weighted moving average
                     (default: 0.15.)
                      
                 |ewma_alpha2| 
                     parameter |alpha| for the second exponentially weighted moving average
                     (default: 0.015.)
                      
                 |threshold| 
                     threshold when the trader starts to act (default: 0.)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)

                 |creationIntervalDistr| 
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)                     
             """,
             [
              ("orderFactory",           "order.factory.side.Market()",  'Side -> IOrderGenerator'),             
              ('ewma_alpha1',           '0.15',                          'non_negative'),
              ('ewma_alpha2',           '0.015',                         'non_negative'),
              ('threshold',             '0.',                            'non_negative'), 
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)', '() -> TimeInterval'),
             ], 
               globals())
