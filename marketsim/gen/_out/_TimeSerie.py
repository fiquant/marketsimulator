from marketsim import registry
from marketsim.gen._intrinsic.timeserie import _ToRecord_Impl
from marketsim import IObservable
from marketsim import IGraph
from marketsim import IObservable
@registry.expose(["Basic", "TimeSerie"])
class TimeSerie(_ToRecord_Impl):
    """ 
    """ 
    def __init__(self, source = None, graph = None, _digitsToShow = None, _smooth = None):
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.veusz._Graph import Graph as _veusz_Graph
        from marketsim.gen._out._false import false as _false
        self.source = source if source is not None else _const(0.0)
        self.graph = graph if graph is not None else _veusz_Graph()
        self._digitsToShow = _digitsToShow if _digitsToShow is not None else 4
        self._smooth = _smooth if _smooth is not None else _false()
        _ToRecord_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[object],
        'graph' : IGraph,
        '_digitsToShow' : int,
        '_smooth' : IObservable[bool]
    }
    def __repr__(self):
        return "TimeSerie(%(source)s, %(graph)s, %(_digitsToShow)s, %(_smooth)s)" % self.__dict__
    
