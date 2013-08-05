from marketsim import (parts, scheduler, observable, types, meta, defs, _, ops,
                       Side, registry, orderbook, bind, order, mathutils)

from .._generic import Generic
from marketsim.types import *

from .. import _wrap

class FundamentalValue(types.ISingleAssetStrategy):

    def getDefinitions(self):
        return { 
            'side' : parts.side.FundamentalValue(self.fundamentalValue)
        }

    def getImpl(self):
        return Generic(order.factory.Market(_.side, self.volumeDistr),
                       scheduler.Timer(self.creationIntervalDistr))

_wrap.strategy(FundamentalValue, ['Periodic', 'Fundamental Value'], 
             """ Fundamental value strategy believes that an asset should have some specific price 
                 (*fundamental value*) and if the current asset price is lower than the fundamental value 
                 it starts to buy the asset and if the price is higher it starts to sell the asset. 
             
                 It has following parameters: 
                 
                 |creationIntervalDistr| 
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                 
                 |fundamentalValue| 
                     defines fundamental value (default: constant 100)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)
             """,
            [
               ('fundamentalValue',     'ops.constant(100)',            '() -> Price'),
               ('volumeDistr',          'mathutils.rnd.expovariate(1.)','() -> Volume'),
               ('creationIntervalDistr','mathutils.rnd.expovariate(1.)','() -> TimeInterval')
            ], globals())