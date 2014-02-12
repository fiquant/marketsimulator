from marketsim import IFunction
from marketsim import Side
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["Side function", "Noise"])
class Noise_Float(Function[Side]):
    """ 
    """ 
    def __init__(self, side_distribution = None):
        from marketsim.gen._out.math.random._uniform import uniform_FloatFloat as _math_random_uniform_FloatFloat
        from marketsim import rtti
        self.side_distribution = side_distribution if side_distribution is not None else _math_random_uniform_FloatFloat(0.0,1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side_distribution' : IFunction[float]
    }
    def __repr__(self):
        return "Noise(%(side_distribution)s)" % self.__dict__
    
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
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._greater import Greater_IFunctionFloatIFunctionFloat as _ops_Greater_IFunctionFloatIFunctionFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.ops._condition import Condition_IFunctionBooleanSideSide as _ops_Condition_IFunctionBooleanSideSide
        return _ops_Condition_IFunctionBooleanSideSide(_ops_Greater_IFunctionFloatIFunctionFloat(self.side_distribution,_constant_Float(0.5)),_side_Sell_(),_side_Buy_())
    
def Noise(side_distribution = None): 
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if side_distribution is None or rtti.can_be_casted(side_distribution, IFunction[float]):
        return Noise_Float(side_distribution)
    raise Exception('Cannot find suitable overload for Noise('+str(side_distribution)+')')
