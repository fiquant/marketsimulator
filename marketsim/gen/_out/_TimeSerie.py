from marketsim.gen._intrinsic.timeserie import _ToRecord_Impl
from marketsim import int
from marketsim import IObservable
from marketsim import IGraph
from marketsim import registry
@registry.expose(["Basic", "TimeSerie"])
class TimeSerie_IObservableAnyIGraphIntInt(_ToRecord_Impl):
    """   Used to specify what data should be collected about order books and traders
    """ 
    def __init__(self, source = None, graph = None, _digitsToShow = None, _smooth = None):
        from marketsim.gen._out._const import const_Float as _const
        from marketsim.gen._out.veusz._graph import Graph_String as _veusz_Graph
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
    
def TimeSerie(source = None,graph = None,_digitsToShow = None,_smooth = None): 
    from marketsim import IObservable
    from marketsim import IGraph
    from marketsim import int
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservable[object]):
        if graph is None or rtti.can_be_casted(graph, IGraph):
            if _digitsToShow is None or rtti.can_be_casted(_digitsToShow, int):
                if _smooth is None or rtti.can_be_casted(_smooth, int):
                    return TimeSerie_IObservableAnyIGraphIntInt(source,graph,_digitsToShow,_smooth)
    raise Exception("Cannot find suitable overload")
