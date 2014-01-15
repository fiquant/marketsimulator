from marketsim import types, meta, flags, event, _, ops

from marketsim.gen._out._TimeSerie import TimeSerie as ToRecord

class VolumeLevels(ToRecord):

    def __init__(self, source, graph, _digits = 4, _smooth = False, _volumes = [], _isBuy = 0):
        ToRecord.__init__(self, source, graph, _digits)
        
    @property
    def _volumes(self):
        return self.source.dataSource.volumes
    
    @property
    def _isBuy(self):
        return 1 if self.source.dataSource.queue.side == types.Side.Buy else 0

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
