from marketsim import scheduler, meta, types, Method

class TimeSerie(object):
    
    def __init__(self, source, label):
        self.label = label
        self._sched = scheduler.current()
        self._source = source
        self._wakeUp = Method(self, '_wakeUp_impl')
        self._source.advise(self._wakeUp)
        self.reset()
        
    def _wakeUp_impl(self, _):
        """ Called when the source has changed
        """
        x = self._source.value
        if x is not None: # for the moment we don't know what to do with breaks in data
            self._data.append((self._sched.currentTime, x))
            # we should also filter out constant segmemnts
            self._changes.append((self._sched.currentTime, x))
        
    @property 
    def _alias(self):
        return self.label + "'"
        
    @_alias.setter
    def _alias(self, value):
        self.label = value
        
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
        
    _properties = { "source" : types.IObservable, "label" : str }
    
    @property    
    def data(self):
        return self._data
    
    def drop(self): # later a more sophisticated protocol would be introduced
        self._data = []
        
class Graph(object):
    
    def __init__(self, label, series=None):
        self.label = label
        self.series = series if series else []
        
    def addTimeSerie(self, source):
        """ Adds a time serie to the graph
        source should be a source of events (so to have advise method) 
        and have a value property 
        """
        label = source.label
        self.series.append(TimeSerie(source, label))
        
    _properties = {"series": meta.listOf(TimeSerie), "label" : str }
    
    @property
    def _alias(self):
        return self.label
    
    @_alias.setter
    def _alias(self, value):
        self.label = value
        
    def addTimeSeries(self, series):
        for x in series:
            self.addTimeSerie(x)
            
    def __iadd__(self, series):
        self.addTimeSeries(series)
        return self

    