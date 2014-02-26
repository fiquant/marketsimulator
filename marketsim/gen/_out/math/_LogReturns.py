from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import context
@registry.expose(["Basic", "LogReturns"])
class LogReturns_IObservableFloatFloat(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None, timeframe = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        self.x = x if x is not None else _const_Float(1.0)
        self.timeframe = timeframe if timeframe is not None else 10.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat,
        'timeframe' : float
    }
    def __repr__(self):
        return "LogReturns_{%(timeframe)s}(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.math._log import Log_Float as _math_Log_Float
        from marketsim.gen._out.ops._div import Div_IObservableFloatIObservableFloat as _ops_Div_IObservableFloatIObservableFloat
        from marketsim.gen._out.math._lagged import Lagged_IObservableFloatFloat as _math_Lagged_IObservableFloatFloat
        return _math_Log_Float(_ops_Div_IObservableFloatIObservableFloat(self.x,_math_Lagged_IObservableFloatFloat(self.x,self.timeframe)))
    
def LogReturns(x = None,timeframe = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return LogReturns_IObservableFloatFloat(x,timeframe)
    raise Exception('Cannot find suitable overload for LogReturns('+str(x) +':'+ str(type(x))+','+str(timeframe) +':'+ str(type(timeframe))+')')
