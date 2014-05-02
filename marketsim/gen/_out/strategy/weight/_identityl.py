def identityL(): 
    from marketsim.gen._out.strategy.weight.array._array_identityl import array_IdentityL_ as _strategy_weight_array_array_IdentityL_
    from marketsim import rtti
    return _strategy_weight_array_array_IdentityL_()
    raise Exception('Cannot find suitable overload for identityL('++')')
# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionlistoffloat import IFunctionlistOffloat
from marketsim.gen._intrinsic.strategy.weight import Identity_Impl
from marketsim import listOf
@registry.expose(["Strategy", "IdentityL"])
class IdentityL_ListFloat(IFunctionlistOffloat,Identity_Impl):
    """ **Identity function for an array of floats**
    
    
    Parameters are:
    
    **array**
    """ 
    def __init__(self, array = None):
        self.array = array if array is not None else []
        Identity_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'array' : listOf(float)
    }
    
    
    def __repr__(self):
        return "IdentityL(%(array)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim import listOf
        rtti.typecheck(listOf(float), self.array)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        
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
        Identity_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Identity_Impl.reset(self)
    
def IdentityL(array = None): 
    from marketsim import listOf
    from marketsim import rtti
    if array is None or rtti.can_be_casted(array, listOf(float)):
        return IdentityL_ListFloat(array)
    raise Exception('Cannot find suitable overload for IdentityL('+str(array) +':'+ str(type(array))+')')
