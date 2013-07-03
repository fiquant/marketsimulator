from marketsim import (event, bind, scheduler, meta, types, Event, 
                       defs, _, ops, registry, mathutils)

from _orderbook import Price
from _ewma import EWMA
from _computed import OnEveryDt

class TwoPointFold(types.Observable):
    
    def __init__(self, source, folder):
        types.Observable.__init__(self)
        
        self._source = source
        self.folder = folder
        self._event = event.subscribe(source, _(self)._wakeup, self)
        self._previous = None
        self._value = None
        
    def _wakeup(self, _):
        current = self._source()
        if self._previous is not None and current is not None:
            self._value = self.folder(self._previous, current)
            self.fire(self)
        self._previous = current
        
    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value):
        self._source = value
        self._event.switchTo(value)
        
    _properties = { 'source' : types.Observable, 
                    'folder' : meta.function((float,float), float) }
        
    def __call__(self):
        return self._value
    
@registry.expose(alias=["delta+"])
@meta.sig((float, float), float)
def upMovement(previous, current):
    return max(0., current - previous)

@registry.expose(alias=["delta-"])
@meta.sig((float, float), float)
def downMovement(previous, current):
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
                { 'rs' : (EWMA(TwoPointFold(_.source, upMovement), alpha) / 
                          EWMA(TwoPointFold(_.source, downMovement), alpha)), 
                  'price' : Price(orderbook),
                  'source': OnEveryDt(timeframe, _.price) \
                                if timeframe > 0 else\
                            _.price })
    
    
    