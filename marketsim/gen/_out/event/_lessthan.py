# generated with class generator.python.intrinsic_function$Import
from marketsim.gen._intrinsic.event import LessThan_Impl

class LessThan_FloatAny(LessThan_Impl):
    """ 
    """ 
    def __init__(self, bound , target ):
        from marketsim import rtti
        self.bound = bound
        self.target = target
        rtti.check_fields(self)
        LessThan_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'bound' : float,
        'target' : object
    }
    
    
    
    
    def __repr__(self):
        return "LessThan(%(bound)s, %(target)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        self.target.bind_ex(self._ctx_ex)
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
        self.target.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        LessThan_Impl.bind_impl(self, ctx)
    
    def reset(self):
        LessThan_Impl.reset(self)
    
def LessThan(bound = None,target = None): 
    from marketsim import rtti
    if bound is None or rtti.can_be_casted(bound, float):
        if target is None or rtti.can_be_casted(target, object):
            return LessThan_FloatAny(bound,target)
    raise Exception('Cannot find suitable overload for LessThan('+str(bound) +':'+ str(type(bound))+','+str(target) +':'+ str(type(target))+')')
