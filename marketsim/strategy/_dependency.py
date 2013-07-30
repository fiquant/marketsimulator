from marketsim import (parts, scheduler, observable, types, meta, defs, _, ops,
                       Side, registry, orderbook, bind, order, mathutils)

from _periodic import Generic
from marketsim.types import *

import _wrap

class Dependency(types.ISingleAssetStrategy):
    
    def getDefinitions(self):
        orderBook = orderbook.OfTrader()
        return { 
            'dependee' : observable.MidPrice(self.bookToDependOn),
            'side' :     parts.side.Dependency(self.bookToDependOn, self.factor)
        }

    def getImpl(self):
        return Generic(order.factory.Market(_.side, self.volumeDistr),  _.dependee)

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
          ('bookToDependOn','orderbook.OfTrader()',             'IOrderBook'),
          ('factor',        '1.',                               'float'),
          ('volumeDistr',   'mathutils.rnd.expovariate(.1)',    '() -> Volume')
          ], globals())
