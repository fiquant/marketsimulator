from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim import IObservable
from marketsim import float
from marketsim import float
from marketsim import context
@registry.expose(["Basic", "LogReturns"])
class LogReturns(Function[float]):
    """ 
    """ 
    def __init__(self, x = None, timeframe = None):
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        self.x = x if x is not None else _const()
        self.timeframe = timeframe if timeframe is not None else 10.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'timeframe' : float
    }
    def __repr__(self):
        return "LogReturns_{%(timeframe)s}(%(x)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.math._Log import Log as _math_Log
        from marketsim.gen._out.ops._Div import Div as _ops_Div
        from marketsim.gen._out.math._Lagged import Lagged as _math_Lagged
        return _math_Log(_ops_Div(self.x,_math_Lagged(self.x,self.timeframe)))
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
