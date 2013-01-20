import math
from marketsim import types

class ewma(types.UpdatableValue):
    """ Exponentially weighted moving average
    """
    
    def __init__(self, alpha=0.15):
        """ Initializes EWMA with \alpha = alpha
        """
        self.alpha = alpha
        self._avg = None
        
    @property
    def label(self):
        return r"Avg_{\alpha="+str(self.alpha)+"}"
    
    @property
    def jsLabel(self):
        return "EWMA(alpha=" + str(self.alpha) + ")"
        
    _properties = {'alpha' : float}
    
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
            self._avg + (self._lastValue - self._avg)*(1 - (1 - self.alpha)**( t - self._lastTime)) \
            if self._avg is not None else None
    
    def derivativeAt(self, t):
        """ Returns derivative of the average at some time point t >= last update time
        Returns None if no data has come
        """
        if self._avg is None:
            return None
        dt = t - self._lastTime
        return -(self._lastValue - self._avg)*math.log(1 - self.alpha)*(1 - self.alpha)**dt
        
    def update(self, time, value):
        """ Adds point (time, value) to calculate the average
        """
        self._avg = self.at(time) if self._avg is not None else value
        self._lastValue = value
        self._lastTime = time
