def clamp0(): 
    from marketsim.gen._out.strategy.weight.f._f_clamp0 import f_Clamp0_ as _strategy_weight_f_f_Clamp0_
    from marketsim import rtti
    return _strategy_weight_f_f_Clamp0_()
    raise Exception('Cannot find suitable overload for clamp0('++')')
from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim import context
@registry.expose(["Strategy", "Clamp0"])
class Clamp0_Float(IFunctionfloat):
    """ 
    """ 
    def __init__(self, f = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        self.f = f if f is not None else _constant_Float(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'f' : IFunctionfloat
    }
    def __repr__(self):
        return "Clamp0(%(f)s)" % self.__dict__
    
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
        from marketsim.gen._out.ops._add import Add_FloatFloat as _ops_Add_FloatFloat
        from marketsim.gen._out.math._max import Max_FloatFloat as _math_Max_FloatFloat
        from marketsim.gen._out._constant import constant_Int as _constant_Int
        return _ops_Add_FloatFloat(_math_Max_FloatFloat(_constant_Int(0),self.f),_constant_Int(1))
    
def Clamp0(f = None): 
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if f is None or rtti.can_be_casted(f, IFunctionfloat):
        return Clamp0_Float(f)
    raise Exception('Cannot find suitable overload for Clamp0('+str(f) +':'+ str(type(f))+')')
