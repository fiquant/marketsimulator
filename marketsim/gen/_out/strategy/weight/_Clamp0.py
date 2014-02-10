def clamp0(): 
    from marketsim.gen._out.strategy.weight.f._f_clamp0 import f_Clamp0_ as _strategy_weight_f_f_Clamp0
    from marketsim import rtti
    return _strategy_weight_f_f_Clamp0()
    raise Exception("Cannot find suitable overload")
from marketsim import IFunction
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "Clamp0"])
class Clamp0_IFunctionFloat(Function[float]):
    """ 
    """ 
    def __init__(self, f = None):
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim import rtti
        self.f = f if f is not None else _constant(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'f' : IFunction[float]
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
        from marketsim.gen._out.ops._add import Add_IFunctionFloatIFunctionFloat as _ops_Add
        from marketsim.gen._out.math._max import Max_IFunctionFloatIFunctionFloat as _math_Max
        from marketsim.gen._out._constant import constant_Float as _constant
        return _ops_Add(_math_Max(_constant(0),self.f),_constant(1))
    
def Clamp0(f = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if f is None or rtti.can_be_casted(f, IFunction[float]):
        return Clamp0_IFunctionFloat(f)
    raise Exception("Cannot find suitable overload")
