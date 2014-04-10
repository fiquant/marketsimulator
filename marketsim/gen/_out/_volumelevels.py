# generated with class generator.python.intrinsic_function$Import
from marketsim.gen._intrinsic.timeserie import VolumeLevels_Impl
from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._ifunction._ifunctionivolumelevels import IFunctionIVolumeLevels
from marketsim import listOf
from marketsim.gen._out._igraph import IGraph

class volumeLevels_IVolumeLevelsIGraphIntIntListFloatInt(ITimeSerie,VolumeLevels_Impl):
    """ **Time serie holding volume levels of an asset**
    
     Level of volume V is a price at which cumulative volume of better orders is V
    
    Parameters are:
    
    **source**
    
    **graph**
    
    **_digitsToShow**
    
    **_smooth**
    
    **_volumes**
    
    **_isBuy**
    """ 
    def __init__(self, source , graph = None, _digitsToShow = None, _smooth = None, _volumes = None, _isBuy = None):
        from marketsim.gen._out.veusz._graph import Graph_String as _veusz_Graph_String
        from marketsim import deref_opt
        from marketsim import rtti
        self.source = source
        self.graph = graph if graph is not None else deref_opt(_veusz_Graph_String())
        self._digitsToShow = _digitsToShow if _digitsToShow is not None else 4
        self._smooth = _smooth if _smooth is not None else 1
        self._volumes = _volumes if _volumes is not None else [30.0]
        self._isBuy = _isBuy if _isBuy is not None else 1
        rtti.check_fields(self)
        VolumeLevels_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IFunctionIVolumeLevels,
        'graph' : IGraph,
        '_digitsToShow' : int,
        '_smooth' : int,
        '_volumes' : listOf(float),
        '_isBuy' : int
    }
    
    
    
    
    
    
    
    
    
    
    
    
    def __repr__(self):
        return "%(source)s" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self._ctx_ex)
                else:
                    v.bind_ex(self._ctx_ex)
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        self.source.bind_ex(self._ctx_ex)
        self.graph.bind_ex(self._ctx_ex)
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def volumeLevels(source = None,graph = None,_digitsToShow = None,_smooth = None,_volumes = None,_isBuy = None): 
    from marketsim.gen._out._ifunction._ifunctionivolumelevels import IFunctionIVolumeLevels
    from marketsim.gen._out._igraph import IGraph
    from marketsim import listOf
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IFunctionIVolumeLevels):
        if graph is None or rtti.can_be_casted(graph, IGraph):
            if _digitsToShow is None or rtti.can_be_casted(_digitsToShow, int):
                if _smooth is None or rtti.can_be_casted(_smooth, int):
                    if _volumes is None or rtti.can_be_casted(_volumes, listOf(float)):
                        if _isBuy is None or rtti.can_be_casted(_isBuy, int):
                            return volumeLevels_IVolumeLevelsIGraphIntIntListFloatInt(source,graph,_digitsToShow,_smooth,_volumes,_isBuy)
    raise Exception('Cannot find suitable overload for volumeLevels('+str(source) +':'+ str(type(source))+','+str(graph) +':'+ str(type(graph))+','+str(_digitsToShow) +':'+ str(type(_digitsToShow))+','+str(_smooth) +':'+ str(type(_smooth))+','+str(_volumes) +':'+ str(type(_volumes))+','+str(_isBuy) +':'+ str(type(_isBuy))+')')
