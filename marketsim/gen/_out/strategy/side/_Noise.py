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
        from marketsim.gen._out.math.random._uniform import uniform as _math_random_uniform
        from marketsim import rtti
        self.side_distribution = side_distribution if side_distribution is not None else _math_random_uniform(0.0,1.0)
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
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.side._Buy import Buy as _side_Buy
        from marketsim.gen._out.ops._Condition_Side import Condition_Side as _ops_Condition_Side
        from marketsim.gen._out.ops._Greater import Greater as _ops_Greater
        return _ops_Condition_Side(_ops_Greater(self.side_distribution,_constant(0.5)),_side_Sell(),_side_Buy())
    
def Noise(side_distribution = None): 
    from marketsim import float
    from marketsim import IFunction
    from marketsim import rtti
    if side_distribution is None or rtti.can_be_casted(side_distribution, IFunction[float]):
        return Noise_Float(side_distribution)
    raise Exception("Cannot find suitable overload")
