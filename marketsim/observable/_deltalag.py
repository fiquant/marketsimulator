from marketsim import ops, types, event, _, getLabel, registry

import fold

from marketsim.gen._out.observable._Lagged import Lagged

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
    