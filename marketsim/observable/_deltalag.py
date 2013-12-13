from marketsim import ops, types, event, _, getLabel, registry

import fold

class Lagged(fold.Last, ops.Observable[float]):

    def __init__(self, source, timeframe):
        fold.Last.__init__(self, source)
        ops.Observable[float].__init__(self)

        self.timeframe = timeframe
        self.reset()
        self._alias = ['_details', 'Lagged']

    _properties = { 'timeframe' : float }

    def reset(self):
        self._backX = 0

    def at(self, t):
        #print self._backX
        return self._backX

    def _getLabel(self):
        return 'Lagged_{%s}' % self.timeframe

    def _remove(self, x):
        self._backX = x
        self.fire(self)

    def update(self, t, x):
        self._scheduler.scheduleAfter(self.timeframe, _(self, x)._remove)

def DeltaLag(source, timeframe):
    return source - Lagged(source, timeframe)

class Base(ops.Observable[float]):
    
    def __init__(self, source = ops.constant(1.)):
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
        
# TODO: impl = ops.Max(ops.constant(0.), source)

@registry.expose(alias = ['_details', 'movements', "up"])    
class UpMovements(Base):
    
    def __call__(self):
        return max(0, self.source())
        
@registry.expose(alias = ['_details', 'movements', "down"])    
class DownMovements(Base):
    
    def __call__(self):
        return max(0, -self.source())
    