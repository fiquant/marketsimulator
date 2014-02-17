from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Statistics", "StdDev"])
class StdDev_IObservableFloatFloat(IFunction[float]):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        self.source = source if source is not None else _const_Float(1.0)
        self.timeframe = timeframe if timeframe is not None else 100.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'timeframe' : float
    }
    def __repr__(self):
        return "\\sqrt{\\sigma^2_{n=%(timeframe)s}(%(source)s)}" % self.__dict__
    
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
        from marketsim.gen._out.math._sqrt import Sqrt_IFunctionFloat as _math_Sqrt_IFunctionFloat
        from marketsim.gen._out.math.Moving._var import Var_IObservableFloatFloat as _math_Moving_Var_IObservableFloatFloat
        return _math_Sqrt_IFunctionFloat(_math_Moving_Var_IObservableFloatFloat(self.source))
    
def StdDev(source = None,timeframe = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservable[float]):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return StdDev_IObservableFloatFloat(source,timeframe)
    raise Exception('Cannot find suitable overload for StdDev('+str(source)+','+str(timeframe)+')')
