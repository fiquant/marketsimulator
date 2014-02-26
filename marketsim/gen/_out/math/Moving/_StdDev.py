from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev_IObservableFloatFloat(IFunctionfloat):
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
        'source' : IObservablefloat,
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
        from marketsim.gen._out.math._sqrt import Sqrt_Float as _math_Sqrt_Float
        from marketsim.gen._out.math.moving._var import Var_IObservableFloatFloat as _math_Moving_Var_IObservableFloatFloat
        return _math_Sqrt_Float(_math_Moving_Var_IObservableFloatFloat(self.source,self.timeframe))
    
def StdDev(source = None,timeframe = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservablefloat):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return StdDev_IObservableFloatFloat(source,timeframe)
    raise Exception('Cannot find suitable overload for StdDev('+str(source) +':'+ str(type(source))+','+str(timeframe) +':'+ str(type(timeframe))+')')
