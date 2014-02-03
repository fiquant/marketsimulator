from marketsim import registry
from marketsim.gen._intrinsic.timeserie import _ToRecord_Impl
from marketsim import IObservable
from marketsim import IGraph
from marketsim import int
from marketsim import int
@registry.expose(["Basic", "TimeSerie"])
class TimeSerie(_ToRecord_Impl):
    """   Used to specify what data should be collected about order books and traders
    """ 
    def __init__(self, source = None, graph = None, _digitsToShow = None, _smooth = None):
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.veusz._Graph import Graph as _veusz_Graph
        from marketsim import rtti
        self.source = source if source is not None else _const(0.0)
        self.graph = graph if graph is not None else _veusz_Graph()
        self._digitsToShow = _digitsToShow if _digitsToShow is not None else 4
        self._smooth = _smooth if _smooth is not None else 1
        rtti.check_fields(self)
        _ToRecord_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[object],
        'graph' : IGraph,
        '_digitsToShow' : int,
        '_smooth' : int
    }
    def __repr__(self):
        return "%(source)s" % self.__dict__
    
