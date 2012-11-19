import math
from marketsim import getLabel
from marketsim.scheduler import world

from _computed import OnEveryDt

class ewma(object):
    """ Exponentially weighted moving average
    """
    
    def __init__(self, alpha):
        """ Initializes EWMA with \alpha = alpha
        """
        self._alpha = alpha
        self._avg = None
        self.label = r"Avg_{\alpha="+str(alpha)+"}"
        
    @property 
    def value(self):
        """ Returns average value at the last update point 
        """
        return self._avg
        
    def at(self, t):
        """ Returns value of the average at some time point t >= last update time
        Returns None if no data has come
        """
        return \
            self._avg + (self._lastValue - self._avg)*(1 - (1 - self._alpha)**( t - self._lastTime)) \
            if self._avg is not None else None
    
    def derivativeAt(self, t):
        """ Returns derivative of the average at some time point t >= last update time
        Returns None if no data has come
        """
        if self._avg is None:
            return None
        dt = t - self._lastTime
        return -(self._lastValue - self._avg)*math.log(1 - self._alpha)*(1 - self._alpha)**dt
        
    def update(self, time, value):
        """ Adds point (time, value) to calculate the average
        """
        self._avg = self.at(time) if self._avg is not None else value
        self._lastValue = value
        self._lastTime = time
        
class derivative(object):
    
    def __init__(self, src):
        self._src = src
        self.update = self._src.update
        self.at = self._src.derivativeAt
        
class Fold(object):
    """ Folds values from some source using a time-dependent accumulator....
    """
    
    def __init__(self, source, acc):
        """ Initializes folder with source of values and accumulator object        
        """
        self._acc = acc
        source.on_changed += lambda _: acc.update(world.currentTime, source.value)
        self.label = getLabel(acc) + "(" + getLabel(source) + ")"
        
    @property
    def value(self):
        """ Returns value from the accumulator corresponding to the current time
        """
        return self._acc.at(world.currentTime)
    
    def __call__(self):
        """ Returns value from the accumulator corresponding to the current time
        """
        return self.value
    
def EWMA(source, alpha=0.15):
    """ Creates a folder with exponential weighted moving average as accumulator
    alpha - parameter for ewma
    """
    return Fold(source, ewma(alpha))

def dEWMA(source, alpha=0.15):
    """ Creates a folder with derivative of exponential weighted moving average as accumulator
    alpha - parameter for ewma
    """
    return Fold(source, derivative(ewma(alpha)))

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

def trend(source, alpha=0.015):
    return OnEveryDt(1, dEWMA(source, alpha))

