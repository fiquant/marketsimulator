from marketsim import types, meta

class ToRecord(object):  # TODO: should the source be split into dataSource and eventSource?
    
    def __init__(self, source, graph):
        self.source = source
        self.graph = graph
        
    _properties = { 'source' : types.IObservable, 
                    'graph'  : types.IGraph }



class Holder(object):
    
    def __init__(self, timeseries = []):
        if type(timeseries) is dict: 
            timeseries = [ToRecord(k,v) for k,v in timeseries.iteritems()]
        self._timeseries = timeseries
        
    def bind(self, context):
        for x in self._timeseries:
            x.graph.addTimeSerie(x.source)

    @property
    def timeseries(self):
        return self._timeseries
    
    @timeseries.setter
    def timeseries(self, value):
        old = set(self._timeseries)
        new = set(value)
        for x in old - new:
            x.graph.removeTimeSerie(x.source)
        for x in new - old:
            x.graph.addTimeSerie(x.source)
        self._timeseries = value
        
    def addTimeSerie(self, source, graph):
        graph.addTimeSerie(source)
        self._timeseries.append(ToRecord(source, graph))
        
    _properties = {'timeseries' : meta.listOf(ToRecord) }
