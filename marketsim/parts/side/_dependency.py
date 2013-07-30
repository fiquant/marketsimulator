from marketsim import (Side, observable, registry, meta, ops, _, orderbook, types)
from marketsim.types import *

import _wrap
from _fv import FundamentalValue
    
class Dependency(ops.Observable[Side]):

    def getImpl(self):    
        return FundamentalValue(observable.MidPrice(self.bookToDependOn) * self.factor, self.orderBook)
    
_wrap.function(Dependency, ['Dependency side'], 
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
         """,
         [
          ('bookToDependOn','orderbook.OfTrader()',             'types.IOrderBook'),
          ('factor',        '1.',                               'float'),
          ('orderBook',     'orderbook.OfTrader()',             'types.IOrderBook'),
          ], globals())
