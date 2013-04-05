from marketsim import getLabel, mathutils, scheduler, meta, types, Method

from _computed import OnEveryDt
        
class derivative(types.IUpdatableValue):
    
    def __init__(self, source):
        self.source = source
        self.update = self.source.update
        self.at = self.source.derivativeAt
        self.derivativeAt = self.at  # temporary hack 
        self.reset = self.source.reset
        self.label = "d(" + source.label + ")"
        
    _properties = { "source" : types.IUpdatableValue }
    
    
class Fold(object):
    """ Folds values from some source using a time-dependent accumulator....
    """
    
    def __init__(self, source, folder):
        """ Initializes folder with source of values and accumulator object        
        """
        self._scheduler = scheduler.current()
        self._acc = folder
        self.label = getLabel(folder) + "(" + getLabel(source) + ")"
        self._source = source
        self._update = Method(self, '_update_impl')
        self._source.on_changed += self._update
            
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
        self._source.on_changed -= self._update
        self._source = value
        self._source.on_changed += self._update
            
    def reset(self):
        self._acc.reset()
                
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

