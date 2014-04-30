# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._intrinsic.timeserie import ToRecord_Impl
from marketsim.gen._out._iobservable._iobservableobject import IObservableobject
from marketsim.gen._out._igraph import IGraph
@registry.expose(["Basic", "TimeSerie"])
class TimeSerie_IObservableAnyIGraphIntInt(ITimeSerie,ToRecord_Impl):
    """ **Time serie to store and render it after on a graph**
    
      Used to specify what data should be collected about order books and traders
    
    Parameters are:
    
    **source**
    
    **graph**
    
    **_digitsToShow**
    
    **_smooth**
    """ 
    def __init__(self, source = None, graph = None, _digitsToShow = None, _smooth = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim.gen._out.veusz._graph import Graph_String as _veusz_Graph_String
        from marketsim import rtti
        self.source = source if source is not None else deref_opt(_const_Float(0.0))
        self.graph = graph if graph is not None else deref_opt(_veusz_Graph_String())
        self._digitsToShow = _digitsToShow if _digitsToShow is not None else 4
        self._smooth = _smooth if _smooth is not None else 1
        rtti.check_fields(self)
        ToRecord_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservableobject,
        'graph' : IGraph,
        '_digitsToShow' : int,
        '_smooth' : int
    }
    
    
    
    
    
    
    
    
    def __repr__(self):
        return "%(source)s" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.source.bind_ex(self._ctx_ex)
        self.graph.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.source.reset_ex(generation)
        self.graph.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
def TimeSerie(source = None,graph = None,_digitsToShow = None,_smooth = None): 
    from marketsim.gen._out._iobservable._iobservableobject import IObservableobject
    from marketsim.gen._out._igraph import IGraph
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservableobject):
        if graph is None or rtti.can_be_casted(graph, IGraph):
            if _digitsToShow is None or rtti.can_be_casted(_digitsToShow, int):
                if _smooth is None or rtti.can_be_casted(_smooth, int):
                    return TimeSerie_IObservableAnyIGraphIntInt(source,graph,_digitsToShow,_smooth)
    raise Exception('Cannot find suitable overload for TimeSerie('+str(source) +':'+ str(type(source))+','+str(graph) +':'+ str(type(graph))+','+str(_digitsToShow) +':'+ str(type(_digitsToShow))+','+str(_smooth) +':'+ str(type(_smooth))+')')
