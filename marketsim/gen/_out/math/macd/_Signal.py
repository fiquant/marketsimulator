from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import context
@registry.expose(["MACD", "Signal"])
class Signal_IObservableFloatFloatFloatFloatFloat(IDifferentiable):
    """ 
    """ 
    def __init__(self, x = None, slow = None, fast = None, timeframe = None, step = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import call
        from marketsim import rtti
        self.x = x if x is not None else call(_const_Float,1.0)
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
        'x' : IObservablefloat,
        'slow' : float,
        'fast' : float,
        'timeframe' : float,
        'step' : float
    }
    def __repr__(self):
        return "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))" % self.__dict__
    
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
        from marketsim.gen._out.math.ew._avg import Avg_IObservableFloatFloat as _math_EW_Avg_IObservableFloatFloat
        from marketsim.gen._out.observable._oneverydt import OnEveryDt_FloatFloat as _observable_OnEveryDt_FloatFloat
        from marketsim.gen._out.math.macd._macd import MACD_IObservableFloatFloatFloat as _math_macd_MACD_IObservableFloatFloatFloat
        from marketsim import call
        return call(_math_EW_Avg_IObservableFloatFloat,call(_observable_OnEveryDt_FloatFloat,call(_math_macd_MACD_IObservableFloatFloatFloat,self.x,self.slow,self.fast),self.step),(2/((self.timeframe+1))))
    
def Signal(x = None,slow = None,fast = None,timeframe = None,step = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        if slow is None or rtti.can_be_casted(slow, float):
            if fast is None or rtti.can_be_casted(fast, float):
                if timeframe is None or rtti.can_be_casted(timeframe, float):
                    if step is None or rtti.can_be_casted(step, float):
                        return Signal_IObservableFloatFloatFloatFloatFloat(x,slow,fast,timeframe,step)
    raise Exception('Cannot find suitable overload for Signal('+str(x) +':'+ str(type(x))+','+str(slow) +':'+ str(type(slow))+','+str(fast) +':'+ str(type(fast))+','+str(timeframe) +':'+ str(type(timeframe))+','+str(step) +':'+ str(type(step))+')')
