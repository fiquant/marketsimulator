from marketsim import ops, types, event, _, getLabel, scheduler, registry

import fold
import math

@registry.expose(alias = ['Statistics', 'Variance', 'Cumulative'])
class Variance(fold.Last):
    
    def __init__(self, source = ops.constant(1.)):
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
        return '\sigma^2'
        
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
            
@registry.expose(alias = ['Statistics', 'StdDev', 'Cumulative'], 
                 args = (ops.constant(1.),))
def StdDev(source):
    return ops.sqrt(Variance(source))
        
from _ma import MA

@registry.expose(alias = ['Statistics', 'Variance', 'Moving'])
class MovingVariance(ops.Function[float]):
    
    def __init__(self, source = ops.constant(1.), timeframe = 10):
        self.source = source
        self.timeframe = timeframe
        self._mean = MA(source, timeframe)
        self._mean2 = MA(ops.Sqr(source), timeframe)
        
    _properties = { 'source' : types.IObservable[float] }
    
    _internals = ["_mean", '_mean2']
    
    @property
    def label(self):
        return '\sigma^2_{' + getLabel(self.source) + '}^{'+str(self.timeframe)+'}'

    def bind(self, ctx):
        self._scheduler = ctx.world
        
    def __call__(self):
        return self.at(self._scheduler.currentTime)
        
    def at(self, t):
        M2 = self._mean2.at(t)
        M = self._mean.at(t)
        if M2 is not None and t > self._mean.startT:
            var = M2 - M*M
            
            if var < 0: # we have roundings errors
                var = 0
                
            return var 
        else:
            return None
        
@registry.expose(alias = ['Statistics', 'StdDev', 'Moving'], 
                 args = (ops.constant(1.),10))
def StdDevRolling(source, timeframe):
    return ops.sqrt(MovingVariance(source, timeframe))

from _ewma import EWMA
        
@registry.expose(alias = ['Statistics', 'Variance', 'Exponentially weighted'])
class EWMV(fold.Last):
    
    def __init__(self, source = ops.constant(1.), alpha = 0.15):
        fold.Last.__init__(self, source)
        self.alpha = alpha
        self._mean = EWMA(source, alpha) # TODO: handle source and alpha change
        self.reset()
        
    _properties = { 'alpha'  : float }
    
    _internals = ['_mean']
    
    def reset(self):
        self._variance = None
        self._lastTime = None
        self._lastValue = None
    
    @property
    def label(self):
        return '\sigma^2_{' + getLabel(self.source) + '}^{'+ str(self.alpha) +'}'
        
    def at(self, t):
        x = self._lastValue
        if x is not None:
            if self._variance is None:
                self._variance = 0
                self._lastTime = t
            mean = self._mean()
            delta = x - mean
            # NB! this formula is not verified!!!
            alpha = (1 - (1 - self.alpha)**( t - self._lastTime))
            return (1 - alpha) * (self._variance + delta * delta * alpha)
            
    def update(self, time, value):
        self._mean.update(time, value)
        if value is not None:
            self._variance = self.at(time)
            self._lastValue = value
            self._lastTime = time
        
@registry.expose(alias = ['Statistics', 'StdDev', 'Exponentially weighted'], 
                 args = (ops.constant(1.),0.15))
def StdDevEW(source, alpha):    
    return ops.sqrt(EWMV(source, alpha))
    