from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._out.math._macd import macd
from marketsim import context
@registry.expose(["MACD", "Signal"])
class Signal_mathmacdFloatFloat(IDifferentiable):
    """ 
    """ 
    def __init__(self, x = None, timeframe = None, step = None):
        from marketsim.gen._out.math._macd import macd_IObservableFloatFloatFloat as _math_macd_IObservableFloatFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_macd_IObservableFloatFloatFloat())
        self.timeframe = timeframe if timeframe is not None else 9.0
        self.step = step if step is not None else 1.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : macd,
        'timeframe' : float,
        'step' : float
    }
    
    
    
    
    
    
    def __repr__(self):
        return "Signal^{%(timeframe)s}_{%(step)s}(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
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
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim import deref_opt
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim.gen._out.math._value import Value_mathmacd as _math_Value_mathmacd
        from marketsim.gen._out.observable._oneverydt import OnEveryDt_FloatFloat as _observable_OnEveryDt_FloatFloat
        return deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_observable_OnEveryDt_FloatFloat(deref_opt(_math_Value_mathmacd(self.x)),self.step)),(2/((self.timeframe+1)))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def Signal(x = None,timeframe = None,step = None): 
    from marketsim.gen._out.math._macd import macd
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, macd):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            if step is None or rtti.can_be_casted(step, float):
                return Signal_mathmacdFloatFloat(x,timeframe,step)
    raise Exception('Cannot find suitable overload for Signal('+str(x) +':'+ str(type(x))+','+str(timeframe) +':'+ str(type(timeframe))+','+str(step) +':'+ str(type(step))+')')
