class MV_Impl(object):
    
    def __init__(self):
        from marketsim.gen._out.math._sqr import Sqr_IObservableFloat
        self._mean = self.x.Avg
        self._mean2 = self.x.source.Sqr.Moving(self.x.timeframe).Avg

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
