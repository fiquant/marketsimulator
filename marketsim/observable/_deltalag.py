from marketsim import ops, types, event, _, getLabel

import fold

class DeltaLag(fold.Last, ops.Observable[float]):
    
    def __init__(self, source, timeframe):
        fold.Last.__init__(self, source)
        ops.Observable[float].__init__(self)
        
        self.timeframe = timeframe
        self.reset()
        
    _properties = { 'timeframe' : float }
        
    def reset(self):
        self._x = 0
        self._backX = 0
    
    def at(self, t):
        return self._x - self._backX
    
    def _getLabel(self):
        return 'DeltaLag_{' + getLabel(self._source) + '}^{'+str(self.timeframe)+'}'
    
    def _remove(self, x):
        self._backX = x
        self.fire(self)
    
    def update(self, t, x):
        if x is not None:
            self._scheduler.scheduleAfter(self.timeframe, _(self, x)._remove)
            self._x = x
            self.fire(self)

class Base(ops.Observable[float]):
    
    def __init__(self, source):
        ops.Observable[float].__init__(self)
        self._source = source
        self._event = event.subscribe(source, self.fire, self)
        
    _properties = { 'source' : types.IObservable[float] }
    
    @property    
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value):
        self._source = value
        self._event.switchTo(value)
    
class UpMovements(Base):
    
    def __call__(self):
        return max(0, self.source())
        
class DownMovements(Base):
    
    def __call__(self):
        return max(0, -self.source())
    