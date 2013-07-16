from marketsim import (event, bind, scheduler, meta, types, Event, 
                       defs, _, ops, registry, mathutils)

from _orderbook import MidPrice
from _ewma import EWMA
from _computed import OnEveryDt
from _deltalag import DeltaLag, UpMovements, DownMovements

import fold

class _rsi_label(ops.identity):
    
    def __init__(self, target, orderbook, timeframe):
        ops.identity.__init__(self, target)
        self._orderbook = orderbook
        self._timeframe = timeframe
    
    @property    
    def label(self):
        return 'RSI_{' + self._orderbook.label + '}^{'+str(self._timeframe)+'}'

class RSI_Impl(object):
    
    def getDefinitions(self):
        return { 
            'rs' : (EWMA(UpMovements(_.deltas), self.alpha) / 
                    EWMA(DownMovements(_.deltas), self.alpha)), 
            'price' : MidPrice(self.orderbook),
            'deltas': DeltaLag(_.price, self.timeframe) 
        }
    
    def getImpl(self):
        return ops.constant(100.) - (ops.constant(100.) / (ops.constant(1.) + _.rs))    
    
    @property    
    def label(self):
        return 'RSI_{{0}}^{{1}}'.format(self.orderbook.label, self.timeframe)
    
class Base(ops.Function[float]):

    def __init__(self):
        self._definitions = self.getDefinitions()
        self.impl = self.getImpl()
        
    _properties = {'impl' : types.IFunction[float] }
        
    def __call__(self):
        return self.impl()
        
class RSI(Base, RSI_Impl):
    
    def __init__(self, orderbook, timeframe, alpha):
        self.orderbook = orderbook
        self.timeframe = timeframe
        self.alpha = alpha
        Base.__init__(self)

tmpl = """
class %(name)s(Base, %(name)s_Impl):
    
    def __init__(self, %(args)s):
        %(ctor)s
        Base.__init__(self)
"""
 
def wrap(name, fields):
     pass
