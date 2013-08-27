import random
from .._generic import Generic
from marketsim import (parts, order, orderbook, scheduler, mathutils, ops,
                       event, types, registry, meta, defs, _, observable)
from marketsim.types import *
               
from .. import _wrap

class LiquidityProviderSide(types.ISingleAssetStrategy):
    
    def getImpl(self):
        return Generic(self.orderFactory(
                            ops.constant(self.side),
                            parts.price.LiquidityProvider(self.side, 
                                                          self.initialValue, 
                                                          self.priceDistr)), 
                       scheduler.Timer(self.creationIntervalDistr))

_wrap.strategy(LiquidityProviderSide, ['Periodic', 'LiquidityProviderSide'],
             """ Liquidity provider for one side has followng parameters:

                 |side|
                     side of orders to create (default: Side.Sell)
                     
                 |initialValue| 
                     initial price which is taken if orderBook is empty (default: 100)
                     
                 |creationIntervalDistr|
                     defines intervals of time between order creation 
                     (default: exponential distribution with |lambda| = 1)
                     
                 |priceDistr|
                     defines multipliers for current asset price when price of
                     order to create is calculated (default: log normal distribution with 
                     |mu| = 0 and |sigma| = 0.1)
                     
                 |volumeDistr| 
                     defines volumes of orders to create 
                     (default: exponential distribution with |lambda| = 1)

                 It wakes up in moments of time given by *creationIntervalDistr*, checks
                 the last best price of orders in the corresponding queue, takes *initialValue*
                 if it is empty, multiplies it by a value taken from *priceDistr* to obtain price
                 of the order to create, calculates order volume using *volumeDistr*, creates
                 an order via *orderFactoryT(side)* and tells the trader to send it.
             """,
             [
              ('orderFactory',          'order.factory.sideprice.Limit()',      '(IFunction[Side], IFunction[float]) -> IOrderGenerator'),
              ('side',                  'Side.Sell',                            'Side'),
              ('initialValue',          '100',                                  'Price'),
              ('creationIntervalDistr', 'mathutils.rnd.expovariate(1.)',        '() -> TimeInterval'),
              ('priceDistr',            'mathutils.rnd.lognormvariate(0., .1)', '() -> float'),
             ],
             globals())
