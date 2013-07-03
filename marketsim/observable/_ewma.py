import math
from marketsim import event, types, registry, ops, _, getLabel

class Fold(ops.Function[float]):
    """ Aggregates (folds) time-dependent data from *source* using given 
        functional  *folder* (e.g. moving average) defined in derived class
    
    For example ::
    
        price_avg = EWMA(Price(book_A), alpha = 0.15)
        
    creates a observable for a moving average with |alpha| = 0.15 of mid-price of asset *book_A*     
    """
    
    def __init__(self, source):
        """ Initializes folder with source of values and accumulator object        
        """
        self._source = source
        self._event = event.subscribe(self._source, _(self)._update, self)
        
    def bind(self, context): # TODO: we should subscribe to acc and source changed events
        self._scheduler = context.world

    @property
    def label(self):
        return self._getLabel() + "(" + getLabel(self._source) + ")"
            
    _properties = { 'source' : types.IObservable }
    
    def _update(self, _):
        self.update(self._scheduler.currentTime, self._source())
        
    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value):
        self._source = value
        self._event.switchTo(self._source)
            
    def __call__(self):
        """ Returns value from the accumulator corresponding to the current time
        """
        return self.at(self._scheduler.currentTime)

class EWMA(Fold, types.IDifferentiable):
    """ Exponentially weighted moving average
    """
    
    def __init__(self, source, alpha=0.15):
        """ Initializes EWMA with \alpha = alpha
        """
        Fold.__init__(self, source)
        self.alpha = alpha
        self.reset()
        
    def reset(self):
        self._avg = None
        self._lastValue = None
        self._lastTime = None
        
    def _getLabel(self):
        return r"Avg_{"+str(self.alpha)+"}"
    
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

class Derivative(ops.Function[float]):
    
    def __init__(self, source):
        self.source = source
        
    _properties = { 'source' : types.IDifferentiable }
        
    def __call__(self):
        return self.source.derivative()

from _computed import OnEveryDt
    
def dEWMA(source, alpha=0.15):
    """ Creates a folder with derivative of exponential weighted moving average as accumulator
    alpha - parameter for ewma
    """
    return Derivative(EWMA(source, alpha))

def avg(source, alpha=0.15):
    return OnEveryDt(1, EWMA(source, alpha))

def trend(source, alpha=0.015):
    return OnEveryDt(1, dEWMA(source, alpha))
