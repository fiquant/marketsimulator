from marketsim import (event, bind, scheduler, meta, types, Event, 
                       defs, _, ops, registry, mathutils)

from _orderbook import MidPrice
from _ewma import EWMA
from _computed import OnEveryDt
from _deltalag import DeltaLag, UpMovements, DownMovements

import fold

class UpMovement(fold.TwoPoint):
    
    def compute(self, previous, current):
        return max(0., current - previous)

class DownMovement(fold.TwoPoint):
    
    def compute(self, previous, current):
        return max(0., previous - current)

class _rsi_label(ops.identity):
    
    def __init__(self, target, orderbook, timeframe):
        ops.identity.__init__(self, target)
        self._orderbook = orderbook
        self._timeframe = timeframe
    
    @property    
    def label(self):
        return 'RSI_{' + self._orderbook.label + '}^{'+str(self._timeframe)+'}'
    

def RSI(orderbook, timeframe, alpha):
    
    return defs(_rsi_label(
                    ops.constant(100.) - (ops.constant(100.) / (ops.constant(1.) + _.rs)), 
                    orderbook, 
                    timeframe), 
                { 'rs' : (EWMA(UpMovements(_.deltas), alpha) / 
                          EWMA(DownMovements(_.deltas), alpha)), 
                  'price' : MidPrice(orderbook),
                  'deltas': DeltaLag(_.price, timeframe) })
    
    
    