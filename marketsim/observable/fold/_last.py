from marketsim import event, types, ops, _, getLabel

class Last(ops.Function[float]):
    """ Aggregates (folds) time-dependent data from *source* using given 
        functional  *folder* (e.g. moving average) defined in derived class
    
    For example ::
    
        price_avg = EWMA(MidPrice(book_A), alpha = 0.15)
        
    creates a observable for a moving average with |alpha| = 0.15 of mid-price of asset *book_A*     
    """
    
    def __init__(self, source):
        """ Initializes folder with source of values and accumulator object        
        """
        self._source = source
        self._event = event.subscribe(self._source, _(self)._update, self)
    
    @property
    def attributes(self):
        return {}
        
    def bind(self, context): 
        self._scheduler = context.world

    @property
    def label(self):
        return self._getLabel() + "(" + getLabel(self._source) + ")"
            
    _properties = { 'source' : types.IObservable[float] }
    
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
