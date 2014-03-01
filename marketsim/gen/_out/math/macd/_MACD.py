from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import context
@registry.expose(["MACD", "MACD"])
class MACD_IObservableFloatFloatFloat(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None, slow = None, fast = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_const_Float(1.0))
        self.slow = slow if slow is not None else 26.0
        self.fast = fast if fast is not None else 12.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat,
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
        from marketsim.gen._out.ops._sub import Sub_FloatFloat as _ops_Sub_FloatFloat
        from marketsim.gen._out.math._avg import Avg_EW as _math_Avg_EW
        from marketsim.gen._out._ew import EW_IObservableFloatFloat as _EW_IObservableFloatFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Sub_FloatFloat(deref_opt(_math_Avg_EW(deref_opt(_EW_IObservableFloatFloat(self.x,(2.0/((self.fast+1))))))),deref_opt(_math_Avg_EW(deref_opt(_EW_IObservableFloatFloat(self.x,(2.0/((self.slow+1)))))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def MACD(x = None,slow = None,fast = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        if slow is None or rtti.can_be_casted(slow, float):
            if fast is None or rtti.can_be_casted(fast, float):
                return MACD_IObservableFloatFloatFloat(x,slow,fast)
    raise Exception('Cannot find suitable overload for MACD('+str(x) +':'+ str(type(x))+','+str(slow) +':'+ str(type(slow))+','+str(fast) +':'+ str(type(fast))+')')
