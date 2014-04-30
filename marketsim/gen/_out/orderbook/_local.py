# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._intrinsic.orderbook.local import Local_Impl
from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import listOf
@registry.expose(["Asset", "Local"])
class Local_StringFloatIntListITimeSerie(IOrderBook,Local_Impl):
    """ **Order book for a single asset in a market.**
    
     Maintains two order queues for orders of different sides
    
    Parameters are:
    
    **name**
    
    **tickSize**
    
    **_digitsToShow**
    
    **timeseries**
    """ 
    def __init__(self, name = None, tickSize = None, _digitsToShow = None, timeseries = None):
        from marketsim import rtti
        self.name = name if name is not None else "-orderbook-"
        self.tickSize = tickSize if tickSize is not None else 0.01
        self._digitsToShow = _digitsToShow if _digitsToShow is not None else 2
        self.timeseries = timeseries if timeseries is not None else []
        rtti.check_fields(self)
        Local_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'name' : str,
        'tickSize' : float,
        '_digitsToShow' : int,
        'timeseries' : listOf(ITimeSerie)
    }
    
    
    
    
    
    
    
    
    def __repr__(self):
        return "%(name)s" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        for x in self.timeseries: x.bind_ex(self._ctx_ex)
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
        for x in self.timeseries: x.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
def Local(name = None,tickSize = None,_digitsToShow = None,timeseries = None): 
    from marketsim.gen._out._itimeserie import ITimeSerie
    from marketsim import listOf
    from marketsim import rtti
    if name is None or rtti.can_be_casted(name, str):
        if tickSize is None or rtti.can_be_casted(tickSize, float):
            if _digitsToShow is None or rtti.can_be_casted(_digitsToShow, int):
                if timeseries is None or rtti.can_be_casted(timeseries, listOf(ITimeSerie)):
                    return Local_StringFloatIntListITimeSerie(name,tickSize,_digitsToShow,timeseries)
    raise Exception('Cannot find suitable overload for Local('+str(name) +':'+ str(type(name))+','+str(tickSize) +':'+ str(type(tickSize))+','+str(_digitsToShow) +':'+ str(type(_digitsToShow))+','+str(timeseries) +':'+ str(type(timeseries))+')')
