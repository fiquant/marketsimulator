from marketsim import scheduler, meta, types, bind

class TimeSerie(object):
    """ Listens to an observable and accumulates its values with time stamps
    """
    
    def __init__(self, source):
        self._source = source
        self._sched = scheduler.current()
        self._wakeUp = bind.Method(self, '_wakeUp_impl')
        self._source.advise(self._wakeUp)
        self.reset()
        
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
        self._source.advise(self._wakeUp)
        
    _properties = { "source" : types.IObservable }
    
    @property    
    def data(self):
        return self._data
    
    def drop(self): # later a more sophisticated protocol would be introduced
        self._data = []
        
class Graph(types.IGraph):
    """ Generic 2D graph to be rendered by means of javascript libraries
    """
    
    def __init__(self, label="", _series=None):
        self.label = label
        self._series = _series if _series else []
        
    def addTimeSerie(self, source):
        """ Adds a time serie to the graph
        source should be a source of events (so to have advise method) 
        and have a value property 
        """
        self._series.append(TimeSerie(source))
        
    def removeTimeSerie(self, source):
        series = [x for x in self._series if x.source is not source]
        
    _properties = {"_series": meta.listOf(TimeSerie) }

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

    