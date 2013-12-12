from marketsim import ops, types, event, _, getLabel,  registry

import fold
import math

from _misc import Sqr

from marketsim.gen._out.observable.Cumulative._Var import Var as Variance
from marketsim.gen._out.observable.Cumulative._StdDev import StdDev

from _ma import MA

@registry.expose(alias = ['Statistics', 'Variance', 'Moving'])
class MovingVariance(ops.Function[float]):
    
    def __init__(self, source = ops.constant(1.), timeframe = 10):
        self.source = source
        self.timeframe = timeframe
        self._mean = MA(source, timeframe)
        self._mean2 = MA(Sqr(source), timeframe)
        
    _properties = { 'source' : types.IObservable[float] }
    
    _internals = ["_mean", '_mean2']
    
    @property
    def label(self):
        return '\sigma^2_{' + getLabel(self.source) + '}^{'+str(self.timeframe)+'}'

    def __repr__(self):
        return  self.label

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
    return ops.Sqrt(MovingVariance(source, timeframe))

from _ewma import EWMA

from marketsim.gen._out.observable.EW._Var import Var as EWMV
from marketsim.gen._out.observable.EW._StdDev import StdDev as StdDevEW

    