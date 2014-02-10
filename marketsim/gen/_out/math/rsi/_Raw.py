from marketsim import IObservable
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["RSI", "Raw"])
class Raw_IObservableFloatFloatFloat(Function[float]):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None, alpha = None):
        from marketsim.gen._out._const import const_Float as _const
        from marketsim import rtti
        self.source = source if source is not None else _const(1.0)
        self.timeframe = timeframe if timeframe is not None else 10.0
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'timeframe' : float,
        'alpha' : float
    }
    def __repr__(self):
        return "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)" % self.__dict__
    
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
        from marketsim.gen._out.ops._div import Div_IFunctionFloatIFunctionFloat as _ops_Div
        from marketsim.gen._out.math.EW._avg import Avg_IObservableFloatFloat as _math_EW_Avg
        from marketsim.gen._out.math._upmovements import UpMovements_IObservableFloatFloat as _math_UpMovements
        from marketsim.gen._out.math._downmovements import DownMovements_IObservableFloatFloat as _math_DownMovements
        return _ops_Div(_math_EW_Avg(_math_UpMovements(self.source,self.timeframe),self.alpha),_math_EW_Avg(_math_DownMovements(self.source,self.timeframe),self.alpha))
    
def Raw(source = None,timeframe = None,alpha = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservable[float]):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            if alpha is None or rtti.can_be_casted(alpha, float):
                return Raw_IObservableFloatFloatFloat(source,timeframe,alpha)
    raise Exception("Cannot find suitable overload")
