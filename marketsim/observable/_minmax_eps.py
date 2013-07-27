from marketsim import types, event, _, ops

class MaxEpsilon(ops.Observable[float]):
    """ Observable that fires if underlying source value becomes greater previous maximum plus some epsilon
    """
    
    def __init__(self, source, epsilon):
        ops.Observable[float].__init__(self)
        self.source = source
        self.epsilon = epsilon
        
    _properties = { 'source' : types.IObservable[float], 
                    'epsilon': types.IFunction[float] }
        
    def _subscribe(self):
        self.value = self.source()
        self._handler = _(self)._fire
        if self.value is not None:
            self._handler = event.GreaterThan(self.value + self.epsilon(), self._handler)
        self.source += self._handler
        
    def bind(self, ctx):
        self._subscribe()
        
    def __call__(self):
        return self.value
        
    def _fire(self, dummy):
        if self.source() is not None:
            self.source -= self._handler
            self._subscribe()
            self.fire(dummy)
        
    @property
    def label(self):
        return "Max^{" + self.source.label + "}_{\epsilon}"
    
    @property
    def attributes(self):
        return {}
        
class MinEpsilon(ops.Observable[float]):
    """ Observable that fires if underlying source value becomes less than previous minimum minus some epsilon
    """
    
    def __init__(self, source, epsilon):
        ops.Observable[float].__init__(self)
        self.source = source
        self.epsilon = epsilon
        
    _properties = { 'source' : types.IObservable[float], 
                    'epsilon': types.IFunction[float] }
        
    def _subscribe(self):
        self.value = self.source()
        self._handler = _(self)._fire
        if self.value is not None:
            self._handler = event.LessThan(self.value - self.epsilon(), self._handler)
        self.source += self._handler
        
    def bind(self, ctx):
        self._subscribe()
        
    def __call__(self):
        return self.value
        
    def _fire(self, dummy):
        if self.source() is not None:
            self.source -= self._handler
            self._subscribe()
            self.fire(dummy)
        
    @property
    def label(self):
        return "Min^{" + self.source.label + "}_{\epsilon}"
    
    @property
    def attributes(self):
        return {}
        
