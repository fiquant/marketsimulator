from marketsim import (parts, scheduler, observable, types, meta, _,
                       Side, registry, orderbook, bind, order, mathutils)

from .._generic import Generic
from marketsim.types import *
from .. import _wrap

class MeanReversion(types.ISingleAssetStrategy):

    def getImpl(self):

        return Generic(self.orderFactory(
                            parts.side.MeanReversion(self.ewma_alpha)), 
                       scheduler.Timer(self.creationIntervalDistr))

_wrap.strategy(MeanReversion, ['Periodic', 'Mean reversion'], 
             """ Mean reversion strategy believes that asset price should return to its average value.
                 It estimates this average using some functional and 
                 if the current asset price is lower than the average
                 it buys the asset and if the price is higher it sells the asset. 
             
                 It has following parameters: 
                 
                 |creationIntervalDistr| 
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                 
                 |ewma_alpha| 
                     |alpha| for exponentially weighted moving average 
                     (default: 0.15)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
             [
              ("orderFactory",  "order.factory.side.Market()",  'IFunction[Side] -> IOrderGenerator'),             
              ('ewma_alpha',            '0.15',                             'non_negative'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',    '() -> TimeInterval')], 
               globals())
