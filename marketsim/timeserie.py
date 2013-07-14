from marketsim import types, meta, flags, event, _

class ToRecord(types.ITimeSerie):  # TODO: should the source be split into dataSource and eventSource?
    
    def __init__(self, source, graph, _digits = 4, _smooth = False):
        self._source = source
        self.graph = graph
        self.attributes = source.attributes
        self._smooth =  1 if 'smooth' in source.attributes and source.attributes['smooth'] else 0
        self._lastPoint = None
        self._event = event.subscribe(source, _(self)._wakeUp, self)
        self.reset()
        
    _properties = { 
                    'source' : types.IObservable[float], 
                    'graph'  : types.IGraph,
                    '_digits': int,
                    "_smooth": int, 
                  }
        

    def bind(self, context):
        self._sched = context.world
        
    @property
    def _digits(self):
        return self._source.digits if 'digits' in dir(self.source) else 4 
    
    @property    
    def _alias(self):
        return [self._source.label]  if '__alias' not in dir(self) else self.__alias
    
    @_alias.setter
    def _alias(self, value):
        self.__alias = value      
        
    @property
    def label(self):
        return self.source.label
    
    def _pushLastPoint(self):
        if self._lastPoint:
            self._data.append(self._lastPoint)
            self._changes.append(self._lastPoint)
            self._lastPoint = None
    
    def _wakeUp(self, _):
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
        self._wakeUp(None)
        self._pushLastPoint()
        return self._changes    
    
    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value):
        self._source = value
        self.__alias = self._source.label        
        self._event.switchTo(self._source)
        
    @property    
    def data(self):
        self._pushLastPoint()
        return self._data
    
    def drop(self): # later a more sophisticated protocol would be introduced
        self._data = []

class VolumeLevels(ToRecord):

    def __init__(self, source, graph, _digits = 4, _smooth = False, _volumes = [], _isBuy = 0):
        ToRecord.__init__(self, source, graph, _digits, _smooth)
        
    @property
    def _volumes(self):
        return self._source.dataSource.volumes
    
    @property
    def _isBuy(self):
        return 1 if self._source.dataSource.side == types.Side.Buy else 0 

    _properties = { "_volumes" : meta.listOf(float), 
                    '_isBuy'   : int }


class Holder(object):
    
    def __init__(self, timeseries = []):
        if type(timeseries) is dict: 
            timeseries = [ToRecord(k,v) for k,v in timeseries.iteritems()]
        self._timeseries = timeseries
        
    @property
    def timeseries(self):
        return self._timeseries
    
    @timeseries.setter
    def timeseries(self, value):
        self._timeseries = value
        
    def addTimeSerie(self, source, graph):
        ts = ToRecord(source, graph)
        self._timeseries.append(ts)
        
    _properties = {'timeseries' : (meta.listOf(ToRecord), flags.collapsed) }
