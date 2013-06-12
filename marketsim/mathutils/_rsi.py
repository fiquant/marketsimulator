import math
from marketsim import types, registry
from _average import ewma

@registry.expose(['Relative strength index'])
class rsi(types.IUpdatableValue):
    """ Relative strength index
    """
    
    def __init__(self, alpha=1.0/14.0):
        """ Initializes EWMA with \alpha = alpha
        """
        self.alpha = alpha
        self.reset()
        
    def reset(self):
        self._RSI = None
        self._lastValue = None
        self._lastTime = None
        self._upAvg = ewma(self.alpha)
        self._downAvg = ewma(self.alpha)
        
    @property
    def label(self):
        return r"RSI_{"+str(self.alpha)+"}"
    
    @property
    def jsLabel(self):
        return "RSI(" + str(self.alpha) + ")"
        
    _properties = {'alpha' : float}
    
    @property 
    def value(self):
        """ Returns average value at the last update point 
        """
        return self._RSI
        
    def at(self, t):
        """ Returns value of the average at some time point t >= last update time
        Returns None if no data has come
        """ 
        rs = self._upAvg.value / self._downAvg.value if self._downAvg.value > 0 else None
        return 100 - 100.0/(1.0 + rs) if rs is not None else None
    
#     # TODO
#     def derivativeAt(self, t):
#         """ Returns derivative of the average at some time point t >= last update time
#         Returns None if no data has come
#         """
#         if self._RSI is None:
#             return None
#         return -1.
        
    def update(self, time, value):
        """ Adds point (time, value) to calculate the average
        """
        if value is not None and self._lastValue is not None:
            self._upAvg.update(time, max(0., value - self._lastValue))
            self._downAvg.update(time, max(0., self._lastValue - value))
            self._RSI = self.at(time)
            self._lastValue = value
            self._lastTime = time
        else:
            self._lastValue = value
            self._lastTime = time