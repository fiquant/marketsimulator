from marketsim import getLabel, mathutils
from marketsim.scheduler import world

from _computed import OnEveryDt
        
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
    return Fold(source, mathutils.ewma(alpha))

def dEWMA(source, alpha=0.15):
    """ Creates a folder with derivative of exponential weighted moving average as accumulator
    alpha - parameter for ewma
    """
    return Fold(source, derivative(mathutils.ewma(alpha)))

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

def trend(source, alpha=0.015):
    return OnEveryDt(1, dEWMA(source, alpha))

