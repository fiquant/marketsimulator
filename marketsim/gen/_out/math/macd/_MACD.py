from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim import IObservable
from marketsim import float
from marketsim import float
from marketsim import float
from marketsim import context
@registry.expose(["MACD", "MACD"])
class MACD_Optional__IObservable__Float____Optional__Float___Optional__Float_(Function[float]):
    """ 
    """ 
    def __init__(self, x = None, slow = None, fast = None):
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        self.x = x if x is not None else _const()
        self.slow = slow if slow is not None else 26.0
        self.fast = fast if fast is not None else 12.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'slow' : float,
        'fast' : float
    }
    def __repr__(self):
        return "MACD_{%(fast)s}^{%(slow)s}(%(x)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.ops._Sub import Sub as _ops_Sub
        from marketsim.gen._out.math.EW._Avg import Avg as _math_EW_Avg
        from marketsim.gen._out.math.EW._Avg import Avg as _math_EW_Avg
        return _ops_Sub(_math_EW_Avg(self.x,(2.0/((self.fast+1)))),_math_EW_Avg(self.x,(2.0/((self.slow+1)))))
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
MACD = MACD_Optional__IObservable__Float____Optional__Float___Optional__Float_
