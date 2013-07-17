from marketsim import types, event, _, ops

class TwoPoint(ops.Observable[float]):
    
    def __init__(self, source):
        ops.Observable[float].__init__(self)
        
        self._source = source
        self._event = event.subscribe(source, _(self)._wakeup, self)
        self._previous = None
        self._value = None
        
    def _wakeup(self, _):
        current = self._source()
        if self._previous is not None and current is not None:
            self._value = self.compute(self._previous, current)
            self.fire(self)
        self._previous = current
        
    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value):
        self._source = value
        self._event.switchTo(value)
        
    _properties = { 'source' : types.IObservable[float] }
        
    def __call__(self):
        return self._value
    
