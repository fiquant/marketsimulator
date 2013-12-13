from marketsim import ops, types, event, _

from marketsim.gen._out.observable.Moving._Avg import Avg
from marketsim.gen._out.observable._Sqr import Sqr

class MV_Impl(object):
    
    def __init__(self):
        self._mean = Avg(self.source, self.timeframe)
        self._mean2 = Avg(Sqr(self.source), self.timeframe)

    _internals = ["_mean", '_mean2']

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
