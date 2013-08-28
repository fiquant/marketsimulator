from .._array import Array
from _lp_side import LiquidityProviderSide
from marketsim import (order, orderbook, mathutils, defs, _,
                       event, types, registry, bind, meta, trader, ops)
from marketsim.types import *
from .. import _wrap

class LiquidityProvider(types.ISingleAssetStrategy):
    
    def getDefinitions(self):
        return { 
                'eventGen'        : self.eventGen, 
                'price'           : self.priceDistr, 
            }
        
    def getImpl(self):
        orderBook = orderbook.OfTrader()
    
        def create(side):
            return LiquidityProviderSide(  _.eventGen,
                                           self.orderFactory,
                                           side, 
                                           self.defaultValue,
                                           _.price)
    
        return Array([
                create(Side.Sell),
                create(Side.Buy)
            ]) 

_wrap.strategy(LiquidityProvider, ['Periodic', 'LiquidityProvider'],
                 """ Liquidity provider is a combination of two LiquidityProviderSide traders 
                     with the same parameters but different trading sides. 
                     
                     It has followng parameters:
                         
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
                """,  
                [
                 ('eventGen',  'event.Every(mathutils.rnd.expovariate(1.))', 'IEvent'),
                 ('orderFactory',          'order.factory.sideprice.Limit()',      '(IFunction[Side], IFunction[float]) -> IOrderGenerator'),
                 ('defaultValue',           '100',                                  'Price'),
                 ('priceDistr',             'mathutils.rnd.lognormvariate(0., .1)', '() -> float'),
                ],
               globals())
