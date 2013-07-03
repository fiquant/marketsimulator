from marketsim import ops, types, event, _, getLabel

import fold

class CMA(fold.Last, types.IDifferentiable):
    
    def __init__(self, source):
        fold.Last.__init__(self, source)
        self.reset()
        
    def reset(self):
        self._x = 0
        self._sum = 0
        self._t = 0
    
    def at(self, t):
        return (self._sum + self._x * (t - self._t)) / t
    
    def _getLabel(self):
        return 'CMA_{' + getLabel(self._source) + '}'
    
    def derivative(self):
        return self.derivativeAt(self._scheduler.currentTime)
    
    def derivativeAt(self, t):
        return self._x / t - (self._x * (t - self._t) + self._sum) / t / t
    
    def update(self, t, x):
        if x is not None:
            self._sum += self._x * (t - self._t)
            self._t = t
            self._x = x
        
    
    