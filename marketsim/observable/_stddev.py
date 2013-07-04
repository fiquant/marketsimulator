from marketsim import ops, types, event, _, getLabel

import fold
import math

class StdDev(fold.Last):
    
    def __init__(self, source):
        fold.Last.__init__(self, source)
        self.reset()
        
    def reset(self):
        self._x = None
        self._t = 0
        self._startT = 0
        self._avg = 0
        self._avg2 = 0
        
    def _at(self, t):
        dX = self._x - self._avg
        dT = t - self._t
        T = t - self._startT
        R = dX * dT / T 
        avg = self._avg + R
        avg2 = self._avg2 + (self._t - self._startT) * dX * R
        return avg, avg2
    
    def at(self, t):
        if self._x is not None and t > self._startT:
            avg, avg2 = self._at(t)
            return math.sqrt(avg2 / (t - self._startT))
        else:
            return None
    
    def _getLabel(self):
        return 'StdDev_{' + getLabel(self._source) + '}'
        
    def update(self, t, x):
        if x is not None:
            if self._x is not None and t > self._startT:
                self._avg, self._avg2 = self._at(t)
            else:
                self._startT = t
            self._t = t
            self._x = x
        
    
    