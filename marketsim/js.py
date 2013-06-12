from marketsim import scheduler, meta, types, bind, flags, event, context

class ITimeSerie(object):
    
    pass

class TimeSerie(ITimeSerie):
    """ Listens to an observable and accumulates its values with time stamps
    """
    
    def __init__(self, _source):
        self._source = _source
        self._sched = scheduler.current()
        self._wakeUp = bind.Method(self, '_wakeUp_impl')
        self._smooth =  1 if 'smooth' in _source.attributes and _source.attributes['smooth'] else 0
        self._lastPoint = None
        self._event = event.subscribe(self._source, self._wakeUp, self)
        self.reset()
        
    def updateContext(self, _):
        pass
        
    def bind(self, context):
        self._sched = context.world
        
    @property
    def _digits(self):
        return self._source.digits if 'digits' in dir(self._source) else 4 
    
    @property    
    def _alias(self):
        return [self._source.label]  if '__alias' not in dir(self) else self.__alias
    
    @_alias.setter
    def _alias(self, value):
        self.__alias = value      
        
    @property
    def label(self):
        return self._source.label
    
    def _pushLastPoint(self):
        if self._lastPoint:
            self._data.append(self._lastPoint)
            self._changes.append(self._lastPoint)
            self._lastPoint = None
    
    def _wakeUp_impl(self, _):
        """ Called when the source has changed
        """
        def appendex(target, (x,y)):
            if target != [] and target[-1][1] == y:
                if self._smooth:
                    self._lastPoint = (x,y)
                return
            self._pushLastPoint()
            target.append((x,y))
                
        x = self._source()
        appendex(self._data, (self._sched.currentTime, x))
        # we should also filter out constant segmemnts
        appendex(self._changes, (self._sched.currentTime, x))
                
    def reset(self):
        self._data = []
        self._changes = []

    def save_state_before_changes(self):
        self._changes = []        
    
    def get_changes(self):
        self._wakeUp_impl(None)
        self._pushLastPoint()
        return self._changes    
    
    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value):
        self._source = value
        self._alias = self._source.label        
        self._event.switchTo(self._source)
        
    _properties = { "_source" : types.IObservable, 
                    "_smooth" : int, 
                    "_digits" : int }
        
    @property    
    def data(self):
        return self._data
    
    def drop(self): # later a more sophisticated protocol would be introduced
        self._data = []
        
class VolumeLevels(TimeSerie):

    def __init__(self, _source):
        TimeSerie.__init__(self, _source)
        
    @property
    def _volumes(self):
        return self._source.dataSource.volumes
    
    @property
    def _isBuy(self):
        return 1 if self._source.dataSource.side == types.Side.Buy else 0 

    _properties = { "_volumes" : meta.listOf(float), 
                    '_isBuy'    : int }

class Graph(types.IGraph):
    """ Generic 2D graph to be rendered by means of javascript libraries
    """
    
    def __init__(self, label="", series=None):
        self.label = label
        self.series = series if series else []
        self._pending = []
        
    def bind(self, ctx):
        self.world = ctx.world
        for p in self._pending:
            self.addTimeSerie(p, ctx)
        self._pending = []
        
    def has(self, source):
        for s in self.series: 
            if s._source is source:
                return True
        return False
        
    def addTimeSerie(self, source, ctx = None):
        """ Adds a time serie to the graph
        source should be a source of events (so to have advise method) 
        and have a value property 
        """
        if "world" not in dir(self):
            self._pending.append(source)
        else:
            if not self.has(source):
                if 'volumeLevels' in source.attributes:
                    ts = VolumeLevels(source)
                else:
                    ts = TimeSerie(source)
                self.series.append(ts)
                if ctx:
                    ctx.apply(ts)
                else:
                    context.bind(ts, { 'world' : self.world })
            
        
    def removeTimeSerie(self, source):
        self.series = [x for x in self.series if x.source is not source]
        
    _properties = {"series": (meta.listOf(ITimeSerie), flags.hidden) }

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

    