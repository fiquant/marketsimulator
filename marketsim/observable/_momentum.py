from marketsim import event, bind, scheduler, meta, types, Event, defs, _, ops, registry, mathutils

from _orderbook import Price
from _ewma import EWMA

class TwoPointFold(types.Observable):
    
    def __init__(self, eventSource, dataSource, folder):
        types.Observable.__init__(self)
        
        self.dataSource = dataSource
        self._eventSource = eventSource
        self.folder = folder
        self._event = event.subscribe(eventSource, _(self)._wakeup, self)
        self._previous = None
        self._value = None
        
    def _wakeup(self, _):
        current = self.dataSource()
        if self._previous is not None and current is not None:
            self._value = self.folder(self._previous, current)
            self.fire(self)
        self._previous = current
        
    @property
    def eventSource(self):
        return self._eventSource
    
    @eventSource.setter
    def eventSource(self, value):
        self._eventSource = value
        self._event.switchTo(value)
        
    _properties = { 'eventSource' : Event, 
                    'dataSource'  : types.IFunction[float],
                    'folder'      : meta.function((float,float), float) }
        
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
                { 'rs' : (EWMA(TwoPointFold(_.timer, _.price, upMovement), alpha) / 
                          EWMA(TwoPointFold(_.timer, _.price, downMovement), alpha)), 
                  'price' : Price(orderbook),
                  'timer' : scheduler.Timer(ops.constant(timeframe)) \
                                if timeframe > 0 else\
                             _.price })
    
    
    