from marketsim import (event, parts, observable, types, meta, defs, _, ops,
                       Side, registry, orderbook, bind, order, mathutils)

from .._generic import Generic
from marketsim.types import *

from .. import _wrap

class Dependency(types.ISingleAssetStrategy):
    
    def getImpl(self):
        return Generic(
                    self.orderFactory(
                            parts.side.Dependency(self.bookToDependOn, self.factor)),
                    self.eventGen)

_wrap.strategy(Dependency, ['Periodic', 'Dependency'],
         """ Dependent price strategy believes that the fair price of an asset *A* 
             is completely correlated with price of another asset *B* and the following relation 
             should be held: *PriceA* = *kPriceB*, where *k* is some factor. 
             It may be considered as a variety of a fundamental value strategy 
             with the exception that it is invoked every the time price of another
             asset *B* changes. 
         
             It has following parameters: 
             
             |bookToDependOn| 
                 reference to order book for another asset used to evaluate fair price of our asset
             
             |factor| 
                 multiplier to obtain fair asset price from the reference asset price
                 
             |volumeDistr| 
                 defines volumes of orders to create 
                 (default: exponential distribution with |lambda| = 1)
         """,
         [
         ('eventGen',  'event.Every(mathutils.rnd.expovariate(1.))', 'IEvent'),
          ("orderFactory",  "order.factory.side.Market()",  'IFunction[Side] -> IOrderGenerator'),             
          ('bookToDependOn','orderbook.OfTrader()',             'IOrderBook'),
          ('factor',        '1.',                               'float'),
          ], globals())
