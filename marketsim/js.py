from marketsim import scheduler, meta, types, bind

class TimeSerie(object):
    """ Listens to an observable and accumulates its values with time stamps
    """
    
    def __init__(self, _source):
        self._source = _source
        self._sched = scheduler.current()
        self._wakeUp = bind.Method(self, '_wakeUp_impl')
        self._smooth =  1 if 'smooth' in _source.attributes and _source.attributes['smooth'] else 0
        self.reset()
        
    def bind(self, context):
        self._sched = context.world
        self._source.advise(self._wakeUp)
        
    @property
    def _digits(self):
        return self._source.digits if 'digits' in dir(self._source) else 4 
    
    @property    
    def _alias(self):
        return [self._source.label]  if '__alias' not in dir(self) else self.__alias
    
    @_alias.setter
    def _alias(self, value):
        self.__alias = value      
        
    def dispose(self):
        self._source.unadvise(self._wakeUp)
        
    @property
    def label(self):
        return self._source.label
    
    def _wakeUp_impl(self, _):
        """ Called when the source has changed
        """
        x = self._source.value
        if x is not None: # for the moment we don't know what to do with breaks in data
            self._data.append((self._sched.currentTime, x))
            # we should also filter out constant segmemnts
            self._changes.append((self._sched.currentTime, x))
                
    def reset(self):
        self._data = []
        self._changes = []

    def save_state_before_changes(self):
        self._changes = []        
    
    def get_changes(self):
        return self._changes    
    
    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value):
        self._source.unadvise(self._wakeUp)
        self._source = value
        self._alias = self._source.label        
        self._source.advise(self._wakeUp)
        
    _properties = { "_source" : types.IObservable, 
                    "_smooth" : int, 
                    "_digits" : int }
        
    @property    
    def data(self):
        return self._data
    
    def drop(self): # later a more sophisticated protocol would be introduced
        self._data = []

class Graph(types.IGraph):
    """ Generic 2D graph to be rendered by means of javascript libraries
    """
    
    def __init__(self, label="", series=None):
        self.label = label
        self.series = series if series else []
        self._pending = []
        
    def bind(self, context):
        self.world = context.world
        for p in self._pending:
            self.addTimeSerie(p)
        self._pending = []
        
    def has(self, source):
        for s in self.series: 
            if s._source is source:
                return True
        return False
        
    def addTimeSerie(self, source):
        """ Adds a time serie to the graph
        source should be a source of events (so to have advise method) 
        and have a value property 
        """
        if "world" not in dir(self):
            self._pending.append(source)
        else:
            if not self.has(source):
                ts = TimeSerie(source)
                self.series.append(ts)
                ts.bind(self)
            
        
    def removeTimeSerie(self, source):
        self.series = [x for x in self.series if x.source is not source]
        
    _properties = {"series": meta.listOf(TimeSerie) }

    @property
    def _alias(self):
        return [self.label]
    
    @_alias.setter
    def _alias(self, value):
        self.label = value[-1]
        
    def addTimeSeries(self, series):
        for x in series:
            self.addTimeSerie(x)
            
    def __iadd__(self, series):
        self.addTimeSeries(series)
        return self

    