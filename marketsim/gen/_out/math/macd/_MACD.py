from marketsim import IFunction
from marketsim import IObservable
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["MACD", "MACD"])
class MACD_IObservableFloatFloatFloat(IFunction[float]):
    """ 
    """ 
    def __init__(self, x = None, slow = None, fast = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        self.x = x if x is not None else _const_Float(1.0)
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
        from marketsim.gen._out.ops._sub import Sub_IFunctionFloatIFunctionFloat as _ops_Sub_IFunctionFloatIFunctionFloat
        from marketsim.gen._out.math.EW._avg import Avg_IObservableFloatFloat as _math_EW_Avg_IObservableFloatFloat
        return _ops_Sub_IFunctionFloatIFunctionFloat(_math_EW_Avg_IObservableFloatFloat(self.x,(2.0/((self.fast+1)))),_math_EW_Avg_IObservableFloatFloat(self.x,(2.0/((self.slow+1)))))
    
def MACD(x = None,slow = None,fast = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservable[float]):
        if slow is None or rtti.can_be_casted(slow, float):
            if fast is None or rtti.can_be_casted(fast, float):
                return MACD_IObservableFloatFloatFloat(x,slow,fast)
    raise Exception('Cannot find suitable overload for MACD('+str(x)+','+str(slow)+','+str(fast)+')')
