# generated with class generator.python.intrinsic_function$Import
from marketsim.gen._intrinsic.veusz import VolumeLevelProxy_Impl

class VolumeLevelProxy_AnyInt(VolumeLevelProxy_Impl):
    """ 
    """ 
    def __init__(self, source , idx ):
        from marketsim import rtti
        self.source = source
        self.idx = idx
        rtti.check_fields(self)
        VolumeLevelProxy_Impl.__init__(self)
    
    
    _properties = {
        'source' : object,
        'idx' : int
    }
    
    
    
    
    
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
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        VolumeLevelProxy_Impl.bind_impl(self, ctx)
    
    def reset(self):
        VolumeLevelProxy_Impl.reset(self)
    
def VolumeLevelProxy(source = None,idx = None): 
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, object):
        if idx is None or rtti.can_be_casted(idx, int):
            return VolumeLevelProxy_AnyInt(source,idx)
    raise Exception('Cannot find suitable overload for VolumeLevelProxy('+str(source) +':'+ str(type(source))+','+str(idx) +':'+ str(type(idx))+')')
