from marketsim.gen._intrinsic.timeserie import _VolumeLevels_Impl
from marketsim import IFunction
from marketsim import VolumeLevels
from marketsim import IGraph
from marketsim import listOf

class volumeLevels(_VolumeLevels_Impl):
    """ 
    """ 
    def __init__(self, source , graph = None, _digitsToShow = None, _smooth = None, _volumes = None, _isBuy = None):
        from marketsim.gen._out.veusz._Graph import Graph as _veusz_Graph
        self.source = source
        self.graph = graph if graph is not None else _veusz_Graph()
        self._digitsToShow = _digitsToShow if _digitsToShow is not None else 4
        self._smooth = _smooth if _smooth is not None else 1
        self._volumes = _volumes if _volumes is not None else [30.0]
        self._isBuy = _isBuy if _isBuy is not None else 1
        _VolumeLevels_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IFunction[VolumeLevels]
        ,
        'graph' : IGraph,
        '_digitsToShow' : int,
        '_smooth' : int,
        '_volumes' : listOf(float),
        '_isBuy' : int
    }
    def __repr__(self):
        return "%(source)s" % self.__dict__
    
