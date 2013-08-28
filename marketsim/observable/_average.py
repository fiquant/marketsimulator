from marketsim import getLabel, ops, mathutils, meta, types, bind, event, _

class derivative(types.IUpdatableValue):
    """ Derivative of some moving average like value. 
    Updated when underlying value is updated.
    """
    
    def __init__(self, source):
        self.source = source
        self.update = _(self.source).update
        self.at = _(self.source).derivativeAt
        self.derivativeAt = _(self.source).at  # temporary hack 
        self.reset = _(self.source).reset
        
    @property
    def label(self):
        return "d(" + self.source.label + ")"
        
    _properties = { "source" : types.IUpdatableValue }
    
    
class Fold(ops.Function[float]):
    """ Aggregates (folds) time-dependent data from *source* using given functional  *folder* (e.g. moving average)
    
    For example ::
    
        price_avg = Fold(MidPrice(book_A), ewma(alpha = 0.15))
        
    creates a observable for a moving average with |alpha| = 0.15 of mid-price of asset *book_A*     
    """
    
    def __init__(self, source, folder):
        """ Initializes folder with source of values and accumulator object        
        """
        self._acc = folder
        self._source = source
        self._event = event.subscribe(self._source, _(self)._update, self)
        self._alias = ['_details', 'fold', 'old']
        
    def bind(self, context): # TODO: we should subscribe to acc and source changed events
        self._scheduler = context.world
        
    @property
    def label(self):
        return getLabel(self._acc) + "(" + getLabel(self._source) + ")"
            
    _properties = { 'source' : types.IObservable[float],
                    'folder' : types.IUpdatableValue }
    
    def _update(self, _):
        self._acc.update(self._scheduler.currentTime, self._source())
        
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
        self._source = value
        self._event.switchTo(self._source)
            
    def __call__(self):
        """ Returns value from the accumulator corresponding to the current time
        """
        return self._acc.at(self._scheduler.currentTime)
    
