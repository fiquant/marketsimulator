from marketsim import (event, bind, meta, types, 
                       defs, _, ops, registry, orderbook, mathutils)

from _orderbook import MidPrice
from _ewma import EWMA
from _computed import OnEveryDt
from _deltalag import Lagged, DeltaLag, UpMovements, DownMovements

import fold

from marketsim.gen._out.observable._Max import Max

import _wrap 
from marketsim.types import *

class RSI(ops.Function[float]):
    
    def getDefinitions(self):
        return { 
            'rs' : (EWMA(Max(ops.constant(0.), MidPrice(self.orderBook) - Lagged(MidPrice(self.orderBook), self.timeframe)), self.alpha) /
                    EWMA(Max(ops.constant(0.), Lagged(MidPrice(self.orderBook), self.timeframe) - MidPrice(self.orderBook)), self.alpha))
        }
        
    def getImpl(self):
        return ops.constant(100.) - (ops.constant(100.) / (ops.constant(1.) + _.rs))

    def __repr__(self):
        return self.label
    
    @property    
    def label(self):
        return 'RSI_{%g}(%s)' % (self.timeframe, self.orderBook.label)
    
_wrap.function(RSI, ["Asset's", "Relative strength index"],
    """ Relative strength index
    """,               
    [
        ('orderBook', 'orderbook.OfTrader()',   'IOrderBook'),
        ('timeframe', 1.,                       'non_negative'),
        ('alpha',     0.15,                     'positive')
    ], globals())


