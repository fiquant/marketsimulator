def atanPow(base = None): 
    from marketsim.gen._out.strategy.weight.f._f_atanpow import f_AtanPow_Float as _strategy_weight_f_f_AtanPow_Float
    from marketsim import rtti
    if base is None or rtti.can_be_casted(base, float):
        return _strategy_weight_f_f_AtanPow_Float(base)
    raise Exception('Cannot find suitable overload for atanPow('+str(base) +':'+ str(type(base))+')')
from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim import context
@registry.expose(["Strategy", "AtanPow"])
class AtanPow_FloatFloat(IFunctionfloat):
    """ 
    """ 
    def __init__(self, f = None, base = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.f = f if f is not None else _constant_Float(1.0)
        self.base = base if base is not None else 1.002
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'f' : IFunctionfloat,
        'base' : float
    }
    def __repr__(self):
        return "AtanPow(%(f)s, %(base)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.math._atan import Atan_Float as _math_Atan_Float
        from marketsim.gen._out.math._pow import Pow_FloatFloat as _math_Pow_FloatFloat
        from marketsim.gen._out._const import const_Float as _const_Float
        return _math_Atan_Float(_math_Pow_FloatFloat(_const_Float(self.base),self.f))
    
def AtanPow(f = None,base = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if f is None or rtti.can_be_casted(f, IFunctionfloat):
        if base is None or rtti.can_be_casted(base, float):
            return AtanPow_FloatFloat(f,base)
    raise Exception('Cannot find suitable overload for AtanPow('+str(f) +':'+ str(type(f))+','+str(base) +':'+ str(type(base))+')')
