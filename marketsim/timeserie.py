from marketsim import types, meta, flags, event, _, ops

from marketsim.gen._out._TimeSerie import TimeSerie as ToRecord
from marketsim.gen._out._volumeLevels import volumeLevels as VolumeLevels

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
        
    _properties = {'timeseries' : (meta.listOf(types.ITimeSerie), flags.collapsed) }
