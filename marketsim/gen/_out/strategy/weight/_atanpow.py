def atanPow(base = None): 
    from marketsim.gen._out.strategy.weight.f._f_atanpow import f_AtanPow_Float as _strategy_weight_f_f_AtanPow_Float
    from marketsim import rtti
    if base is None or rtti.can_be_casted(base, float):
        return _strategy_weight_f_f_AtanPow_Float(base)
    raise Exception('Cannot find suitable overload for atanPow('+str(base) +':'+ str(type(base))+')')
# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Strategy", "AtanPow"])
class AtanPow_FloatFloat(IFunctionfloat):
    """ **scaling function = atan(base^f(x))**
    
    
    Parameters are:
    
    **f**
    	 function to scale 
    
    **base**
    	 base for power function 
    """ 
    def __init__(self, f = None, base = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        self.f = f if f is not None else deref_opt(_constant_Float(1.0))
        self.base = base if base is not None else 1.002
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'f' : IFunctionfloat,
        'base' : float
    }
    
    
    
    
    def __repr__(self):
        return "AtanPow(%(f)s, %(base)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.f.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.f.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
        rtti.typecheck(IFunctionfloat, self.f)
        rtti.typecheck(float, self.base)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.f.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.impl.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        
    
    def getImpl(self):
        from marketsim.gen._out.math._atan import Atan_Float as _math_Atan_Float
        from marketsim.gen._out.math._pow import Pow_FloatFloat as _math_Pow_FloatFloat
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        return deref_opt(_math_Atan_Float(deref_opt(_math_Pow_FloatFloat(deref_opt(_const_Float(self.base)),self.f))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def AtanPow(f = None,base = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if f is None or rtti.can_be_casted(f, IFunctionfloat):
        if base is None or rtti.can_be_casted(base, float):
            return AtanPow_FloatFloat(f,base)
    raise Exception('Cannot find suitable overload for AtanPow('+str(f) +':'+ str(type(f))+','+str(base) +':'+ str(type(base))+')')
