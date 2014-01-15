from marketsim import registry
from marketsim.gen._intrinsic.timeserie import _ToRecord_Impl
from marketsim import IObservable
from marketsim import IGraph
@registry.expose(["Basic", "TimeSerie"])
class TimeSerie(_ToRecord_Impl):
    """ 
    """ 
    def __init__(self, source = None, graph = None, _digitsToShow = None):
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.veusz._Graph import Graph as _veusz_Graph
        self.source = source if source is not None else _const(0.0)
        self.graph = graph if graph is not None else _veusz_Graph()
        self._digitsToShow = _digitsToShow if _digitsToShow is not None else 4
        _ToRecord_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[object],
        'graph' : IGraph,
        '_digitsToShow' : int
    }
    def __repr__(self):
        return "%(source)s" % self.__dict__
    
