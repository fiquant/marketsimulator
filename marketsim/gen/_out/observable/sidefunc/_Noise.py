from marketsim import registry
from marketsim.ops._function import Function
from marketsim import Side
from marketsim import IFunction
from marketsim.gen._out.side._Sell import Sell as _side_Sell
from marketsim.gen._out.side._Buy import Buy as _side_Buy
from marketsim.gen._out._const import const as _const
from marketsim import context
@registry.expose(["Side function", "Noise"])
class Noise(Function[Side]):
    """ 
    """ 
    def __init__(self, side_distribution = None):
        from marketsim.gen._out.mathutils.rnd._uniform import uniform as _mathutils_rnd_uniform
        self.side_distribution = side_distribution if side_distribution is not None else _mathutils_rnd_uniform(0.0,1.0)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side_distribution' : IFunction[float]
    }
    def __repr__(self):
        return "Noise(%(side_distribution)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return (self.side_distribution>_const(0.5))[_side_Sell(), _side_Buy()]
    
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
