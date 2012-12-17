import math

class ewma(object):
    """ Exponentially weighted moving average
    """
    
    def __init__(self, alpha):
        """ Initializes EWMA with \alpha = alpha
        """
        self._alpha = alpha
        self._avg = None
        self.label = r"Avg_{\alpha="+str(alpha)+"}"
        
    _properties = {'alpha' : float}
    
    @property
    def alpha(self):
        return self._alpha
        
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
