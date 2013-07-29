from marketsim import (Side, observable, registry, meta, ops, _, orderbook, types)
from marketsim.types import *

import _wrap
from _fv import FundamentalValue
    
class MeanReversion(ops.Observable[Side]):
    
    def getImpl(self):
        avg = observable.EWMA(observable.MidPrice(self.orderBook), self.ewma_alpha)
        return FundamentalValue(self.orderBook, avg)
    
_wrap.function(MeanReversion, ['MeanReversion side'], 
             """ Mean reversion strategy believes that asset price should return to its average value.
                 It estimates this average using some functional and 
                 if the current asset price is lower than the average
                 it buys the asset and if the price is higher it sells the asset. 
             
                 It has following parameters: 
                 
                 |ewma_alpha| 
                     |alpha| for exponentially weighted moving average 
                     (default: 0.15)
             """,
             [
              ('ewma_alpha',            '0.15',                         'non_negative'),
              ('orderBook',             'orderbook.OfTrader()',         'types.IOrderBook'),
             ],
               globals())
