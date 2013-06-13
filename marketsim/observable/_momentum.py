from marketsim import event, bind, scheduler, meta, types, Event
from marketsim.mathutils import *

from _computed import Price
from _average import Fold

class TwoPointFold(types.IObservable):
    
    def __init__(self, eventSource, dataSource, folder):
        types.IObservable.__init__(self)
        
        self.dataSource = dataSource
        self._eventSource = eventSource
        self.folder = folder
        self._event = event.subscribe(eventSource, bind.Method(self, '_wakeup'), self)
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
                    'dataSource'  : meta.function((), float),
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

class _rsi_sub(sub):
    
    def __init__(self, lhs, rhs, orderbook, timeframe):
        sub.__init__(self, lhs, rhs)
        self._orderbook = orderbook
        self._timeframe = timeframe
        
    @property
    def label(self):
        return 'RSI_{' + self._orderbook.label + '}^{'+str(self._timeframe)+'}'
        

def RSI(orderbook, timeframe, alpha):
    
    price = Price(orderbook)
    timer = scheduler.Timer(constant(timeframe)) if timeframe > 0 else price
    
    ups = TwoPointFold(timer, price, upMovement)
    downs = TwoPointFold(timer, price, downMovement)
    
    ups_ma = Fold(ups, ewma(alpha))
    downs_ma = Fold(downs, ewma(alpha))
    
    rs = div(ups_ma, downs_ma)
    
    return _rsi_sub(constant(100.), div(constant(100.), sum(constant(1.), rs)), orderbook, timeframe)
    
    
    