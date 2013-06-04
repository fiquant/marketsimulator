from marketsim import getLabel, mathutils, scheduler, meta, types, bind

from _computed import OnEveryDt
        
class derivative(types.IUpdatableValue):
    """ Derivative of some moving average like value. 
    Updated when underlying value is updated.
    """
    
    def __init__(self, source):
        self.source = source
        self.update = bind.Method(self.source, 'update')
        self.at = bind.Method(self.source, 'derivativeAt')
        self.derivativeAt = bind.Method(self, 'at')  # temporary hack 
        self.reset = bind.Method(self.source, 'reset')
        
    @property
    def label(self):
        return "d(" + self.source.label + ")"
        
    _properties = { "source" : types.IUpdatableValue }
    
    
class Fold(object):
    """ Aggregates (folds) time-dependent data from *source* using given functional  *folder* (e.g. moving average)
    
    For example ::
    
        price_avg = Fold(Price(book_A), ewma(alpha = 0.15))
        
    creates a observable for a moving average with |alpha| = 0.15 of mid-price of asset *book_A*     
    """
    
    def __init__(self, source, folder):
        """ Initializes folder with source of values and accumulator object        
        """
        self._acc = folder
        self._source = source
        self._update = bind.Method(self, '_update_impl')
        self._source += self._update
        
    def bind(self, context): # TODO: we should subscribe to acc and source changed events
        self._scheduler = context.world
        
    @property
    def label(self):
        return getLabel(self._acc) + "(" + getLabel(self._source) + ")"
            
    _properties = { 'source' : types.IObservable,
                    'folder' : types.IUpdatableValue }
    
    _types = [meta.function((), float)]
    
    def _update_impl(self, _):
        self._acc.update(self._scheduler.currentTime, self._source.value)
        
    @property
    def folder(self):
        return self._acc
    
    @folder.setter
    def folder(self, value):
        self._acc = value
        
    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value):
        self._source -= self._update
        self._source = value
        self._source += self._update
            
    @property
    def value(self):
        """ Returns value from the accumulator corresponding to the current time
        """
        return self._acc.at(self._scheduler.currentTime)
    
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

