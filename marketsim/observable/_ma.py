from marketsim import ops, types, event, _, getLabel

import fold

class MA(fold.Last, types.IDifferentiable):
    
    def __init__(self, source, timeframe):
        fold.Last.__init__(self, source)
        self.timeframe = timeframe
        self.reset()
        
    _properties = { 'timeframe' : float }
        
    def reset(self):
        self._x = None
        self._sum = 0
        self._t = 0
        self._backX = 0
        self._startT = 0
        self._backT = -self.timeframe
    
    def at(self, t):
        T = t - self._startT
        return (self._sum 
                + self._x * (t - self._t) 
                - self._backX * (t - self.timeframe - self._backT)
                ) / min(T, self.timeframe)\
            if T > 0 and self._x is not None else None
    
    def _getLabel(self):
        return 'MA_{' + getLabel(self._source) + '}^{'+str(self.timeframe)+'}'
    
    def derivative(self):
        return self.derivativeAt(self._scheduler.currentTime)
    
    def derivativeAt(self, t):
        T = t - self._startT
        return\
            (self._x / T - (self._x * (t - self._t) + self._sum) / T / T\
                if t - self._startT < self.timeframe else\
             (self._x - self._backX) / self.timeframe)\
        if T > 0 and self._x is not None else None
        
    @property
    def startT(self):
        return self._startT
    
    def _remove(self, dS, t, x):
        self._sum -= dS
        self._backT = t
        self._backX = x
    
    def update(self, t, x):
        if x is not None:
            if self._x is not None:
                dS = self._x * (t - self._t)
                self._sum += dS
                self._scheduler.scheduleAfter(self.timeframe, _(self, dS, t, x)._remove)
            else:
                self._startT = t
            self._t = t
            self._x = x
        
    
    