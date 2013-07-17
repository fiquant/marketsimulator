import math
from marketsim import types, registry, ops

import fold

class EWMA(fold.Last, types.IDifferentiable):
    """ Exponentially weighted moving average
    """
    
    def __init__(self, source, alpha=0.15):
        """ Initializes EWMA with \alpha = alpha
        """
        fold.Last.__init__(self, source)
        self.alpha = alpha
        self.reset()
        
    def reset(self):
        self._avg = None
        self._lastValue = None
        self._lastTime = None
        
    def _getLabel(self):
        return r"Avg_{%s}" % self.alpha
    
    @property
    def jsLabel(self):
        return "EWMA(" + str(self.alpha) + ")"
        
    _properties = {'alpha' : float}
    
    def at(self, t):
        """ Returns value of the average at some time point t >= last update time
        Returns None if no data has come
        """
        return \
            self._avg + (self._lastValue - self._avg)*(1 - (1 - self.alpha)**( t - self._lastTime)) \
            if self._avg is not None else None
    
    def derivative(self):
        return self.derivativeAt(self._scheduler.currentTime)
    
    def derivativeAt(self, t):
        """ Returns derivative of the average at some time point t >= last update time
        Returns None if no data has come
        """
        if self._avg is None:
            return None
        dt = t - self._lastTime
        return  -(self._lastValue - self._avg)*math.log(1 - self.alpha)*(1 - self.alpha)**dt
        
    def update(self, time, value):
        """ Adds point (time, value) to calculate the average
        """
        if value is not None:
            self._avg = self.at(time) if self._avg is not None else value
            self._lastValue = value
            self._lastTime = time


from _computed import OnEveryDt
    
def dEWMA(source, alpha=0.15):
    """ Creates a folder with derivative of exponential weighted moving average as accumulator
    alpha - parameter for ewma
    """
    return ops.Derivative(EWMA(source, alpha))

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

def trend(source, alpha=0.015):
    return OnEveryDt(1, dEWMA(source, alpha))
