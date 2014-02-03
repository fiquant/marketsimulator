from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim import IObservable
from marketsim import float
from marketsim import float
from marketsim import float
from marketsim import float
from marketsim import float
from marketsim import context
@registry.expose(["MACD", "Histogram"])
class Histogram(Function[float]):
    """ 
    """ 
    def __init__(self, x = None, slow = None, fast = None, timeframe = None, step = None):
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        self.x = x if x is not None else _const()
        self.slow = slow if slow is not None else 26.0
        self.fast = fast if fast is not None else 12.0
        self.timeframe = timeframe if timeframe is not None else 9.0
        self.step = step if step is not None else 1.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'slow' : float,
        'fast' : float,
        'timeframe' : float,
        'step' : float
    }
    def __repr__(self):
        return "Histogram^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.ops._Sub import Sub as _ops_Sub
        from marketsim.gen._out.math.macd._MACD import MACD as _math_macd_MACD
        from marketsim.gen._out.math.macd._Signal import Signal as _math_macd_Signal
        return _ops_Sub(_math_macd_MACD(self.x,self.slow,self.fast),_math_macd_Signal(self.x,self.slow,self.fast,self.timeframe,self.step))
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
