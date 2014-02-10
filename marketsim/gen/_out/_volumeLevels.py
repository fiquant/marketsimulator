from marketsim import IFunction
from marketsim import int
from marketsim import IVolumeLevels
from marketsim import IGraph
from marketsim.gen._intrinsic.timeserie import _VolumeLevels_Impl
from marketsim import listOf
from marketsim import float

class volumeLevels_IFunctionIVolumeLevelsIGraphIntIntListFloatInt(_VolumeLevels_Impl):
    """  Level of volume V is a price at which cumulative volume of better orders is V
    """ 
    def __init__(self, source , graph = None, _digitsToShow = None, _smooth = None, _volumes = None, _isBuy = None):
        from marketsim.gen._out.veusz._graph import Graph_String as _veusz_Graph
        from marketsim import rtti
        self.source = source
        self.graph = graph if graph is not None else _veusz_Graph()
        self._digitsToShow = _digitsToShow if _digitsToShow is not None else 4
        self._smooth = _smooth if _smooth is not None else 1
        self._volumes = _volumes if _volumes is not None else [30.0]
        self._isBuy = _isBuy if _isBuy is not None else 1
        rtti.check_fields(self)
        _VolumeLevels_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IFunction[IVolumeLevels],
        'graph' : IGraph,
        '_digitsToShow' : int,
        '_smooth' : int,
        '_volumes' : listOf(float),
        '_isBuy' : int
    }
    def __repr__(self):
        return "%(source)s" % self.__dict__
    
def volumeLevels(source = None,graph = None,_digitsToShow = None,_smooth = None,_volumes = None,_isBuy = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import int
    from marketsim import listOf
    from marketsim import IVolumeLevels
    from marketsim import IGraph
    if source is None or rtti.can_be_casted(source, IFunction[IVolumeLevels]):
        if graph is None or rtti.can_be_casted(graph, IGraph):
            if _digitsToShow is None or rtti.can_be_casted(_digitsToShow, int):
                if _smooth is None or rtti.can_be_casted(_smooth, int):
                    if _volumes is None or rtti.can_be_casted(_volumes, listOf(float)):
                        if _isBuy is None or rtti.can_be_casted(_isBuy, int):
                            return volumeLevels_IFunctionIVolumeLevelsIGraphIntIntListFloatInt(source,graph,_digitsToShow,_smooth,_volumes,_isBuy)
    raise Exception("Cannot find suitable overload")
