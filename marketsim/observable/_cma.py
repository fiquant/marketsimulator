from marketsim import ops, types, event, _, getLabel

import fold

class CMA(fold.Last, types.IDifferentiable):
    
    def __init__(self, source):
        fold.Last.__init__(self, source)
        self.reset()
        
    def reset(self):
        self._x = None
        self._t = 0
        self._startT = 0
        self._avg = 0
    
    def at(self, t):
        T = t - self._startT
        return self._avg + (self._x  - self._avg)* (t - self._t)  / T\
            if T > 0 and self._x is not None else None
    
    def _getLabel(self):
        return 'CMA'
    
    def derivative(self):
        return self.derivativeAt(self._scheduler.currentTime)
    
    def derivativeAt(self, t):
        T = t - self._startT
        d = self._x - self._avg if self._x is not None else None
        return d / T - d * (t - self._t) / T / T\
            if T > 0 and self._x is not None else None
    
    def update(self, t, x):
        if x is not None:
            if self._x is not None and t > self._startT:
                self._avg += (self._x  - self._avg)* (t - self._t) / (t - self._startT)
            else:
                self._startT = t
            self._t = t
            self._x = x
        
    
    