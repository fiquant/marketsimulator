from marketsim import (event, bind, scheduler, meta, types, 
                       defs, _, ops, registry, orderbook, mathutils)

from _orderbook import MidPrice
from _ewma import EWMA
from _computed import OnEveryDt
from _deltalag import DeltaLag, UpMovements, DownMovements

import fold

import _wrap 
from marketsim.types import *

class RSI(ops.Function[float]):
    
    def getDefinitions(self):
        return { 
            'rs' : (EWMA(UpMovements(_.deltas), self.alpha) / 
                    EWMA(DownMovements(_.deltas), self.alpha)), 
            'price' : MidPrice(self.orderBook),
            'deltas': DeltaLag(_.price, self.timeframe) 
        }
        
    def getImpl(self):
        return ops.constant(100.) - (ops.constant(100.) / (ops.constant(1.) + _.rs))    
    
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


