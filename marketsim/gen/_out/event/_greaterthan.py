# generated with class generator.python.intrinsic_function$Import
from marketsim.gen._intrinsic.event import GreaterThan_Impl

class GreaterThan_FloatAny(GreaterThan_Impl):
    """ 
    """ 
    def __init__(self, bound , target ):
        self.bound = bound
        self.target = target
        GreaterThan_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'bound' : float,
        'target' : object
    }
    
    
    
    
    def __repr__(self):
        return "GreaterThan(%(bound)s, %(target)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
    
    def typecheck(self):
        from marketsim import rtti
        rtti.typecheck(float, self.bound)
        rtti.typecheck(object, self.target)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.target.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.registerIn(registry)
                else:
                    v.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        GreaterThan_Impl.bind_impl(self, ctx)
    
    def reset(self):
        GreaterThan_Impl.reset(self)
    
def GreaterThan(bound = None,target = None): 
    from marketsim import rtti
    if bound is None or rtti.can_be_casted(bound, float):
        if target is None or rtti.can_be_casted(target, object):
            return GreaterThan_FloatAny(bound,target)
    raise Exception('Cannot find suitable overload for GreaterThan('+str(bound) +':'+ str(type(bound))+','+str(target) +':'+ str(type(target))+')')
