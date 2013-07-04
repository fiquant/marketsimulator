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
        
    def _increments(self, t, ti, mean, x):
        dX = x - mean
        dT = t - ti
        T = t - self._startT
        R = dX * dT / T 
        return R, (ti - self._startT) * dX * R
        
        
    def _at(self, t):
        dM, dM2 = self._increments(t, self._t, self._avg, self._x)
        return self._avg + dM, self._avg2 + dM2
    
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
                dM, dM2 = self._increments(t, self._t, self._avg, self._x)
                self._avg += dM
                self._avg2 += dM2
            else:
                self._startT = t
            self._t = t
            self._x = x
        
from _ma import MA

class StdDevRolling(ops.Function[float]):
    
    def __init__(self, source, timeframe):
        self.source = source
        self.timeframe = timeframe
        self._mean = MA(source, timeframe)
        self._mean2 = MA(ops.Sqr(source), timeframe)
        
    _properties = { 'source' : types.Observable }
    
    _internals = ["_mean", '_mean2']
    
    @property
    def label(self):
        return 'StdDev_{' + getLabel(self.source) + '}^{'+str(self.timeframe)+'}'

    def bind(self, ctx):
        self._scheduler = ctx.world
        
    def __call__(self):
        return self.at(self._scheduler.currentTime)
        
    def at(self, t):
        M2 = self._mean2.at(t)
        M = self._mean.at(t)
        if M2 is not None and t > self._mean.startT:
            var = M2 - M*M
            
            if var < 1e-2:
                var = 0
                
            return math.sqrt(var) 
        else:
            return None