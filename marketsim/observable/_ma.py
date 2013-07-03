from marketsim import ops, types, event, _, getLabel

import fold

class MA(fold.Last, types.IDifferentiable):
    
    def __init__(self, source, timeframe):
        fold.Last.__init__(self, source)
        self.timeframe = timeframe
        self.reset()
        
    _properties = { 'timeframe' : float }
        
    def reset(self):
        self._x = 0
        self._sum = 0
        self._t = 0
        self._backX = 0
        self._backT = -self.timeframe
    
    def at(self, t):
        return (self._sum 
                + self._x * (t - self._t) 
                - self._backX * (t - self.timeframe - self._backT)
                ) / min(t, self.timeframe) if t > 0 else 0
    
    def _getLabel(self):
        return 'MA_{' + getLabel(self._source) + '}^{'+str(self.timeframe)+'}'
    
    def derivative(self):
        return self._x - self._backX
    
    def _remove(self, dS, t, x):
        self._sum -= dS
        self._backT = t
        self._backX = x
    
    def update(self, t, x):
        if x is not None:
            dS = self._x * (t - self._t)
            self._sum += dS
            self._scheduler.scheduleAfter(self.timeframe, _(self, dS, t, x)._remove)
            self._t = t
            self._x = x
        
    
    