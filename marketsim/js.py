from marketsim import scheduler

class TimeSerie(object):
    
    def __init__(self, source, label, sched = None):
        self.label = label
        self._sched = scheduler.current() if sched is None else sched
        self._source = source
        def wakeUp(_):
            """ Called when the source has chaged
            """
            x = self._source.value
            if x is not None: # for the moment we don't know what to do with breaks in data
                self._data.append((self._sched.currentTime, x))
        
        self._source.advise(wakeUp)
        self.reset()
        
    def reset(self):
        self._data = []
        
    _properties = {}
    
    @property    
    def data(self):
        return self._data
    
    def drop(self): # later a more sophisticated protocol would be introduced
        self._data = []
        
class Graph(object):
    
    def __init__(self, label):
        self.label = label
        self.series = []
        
    def addTimeSerie(self, source):
        """ Adds a time serie to the graph
        source should be a source of events (so to have advise method) 
        and have a value property 
        """
        label = source.label
        self.series.append(TimeSerie(source, label))
        
    _properties = {"series": None}
        
    def addTimeSeries(self, series):
        for x in series:
            self.addTimeSerie(x)
            
    def __iadd__(self, series):
        self.addTimeSeries(series)
        return self

    