# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out.math._rsi import RSI
from marketsim import context
@registry.expose(["RSI", "Raw"])
class Raw_mathRSI(IFunctionfloat):
    """ **Absolute value for Relative Strength Index**
    
    
    Parameters are:
    
    **x**
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._rsi import RSI_IObservableFloatFloatFloat as _math_RSI_IObservableFloatFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_RSI_IObservableFloatFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : RSI
    }
    
    
    def __repr__(self):
        return "Raw(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
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
        from marketsim.gen._out.math._alpha import Alpha_mathRSI as _math_Alpha_mathRSI
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim.gen._out.ops._div import Div_FloatFloat as _ops_Div_FloatFloat
        from marketsim.gen._out.math._downmovements import DownMovements_IObservableFloatFloat as _math_DownMovements_IObservableFloatFloat
        from marketsim.gen._out.math._upmovements import UpMovements_IObservableFloatFloat as _math_UpMovements_IObservableFloatFloat
        from marketsim.gen._out.math._source import Source_mathRSI as _math_Source_mathRSI
        from marketsim.gen._out.math._timeframe import Timeframe_mathRSI as _math_Timeframe_mathRSI
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim import deref_opt
        return deref_opt(_ops_Div_FloatFloat(deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_math_UpMovements_IObservableFloatFloat(deref_opt(_math_Source_mathRSI(self.x)),deref_opt(_math_Timeframe_mathRSI(self.x)))),deref_opt(_math_Alpha_mathRSI(self.x)))))),deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_math_DownMovements_IObservableFloatFloat(deref_opt(_math_Source_mathRSI(self.x)),deref_opt(_math_Timeframe_mathRSI(self.x)))),deref_opt(_math_Alpha_mathRSI(self.x))))))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def Raw(x = None): 
    from marketsim.gen._out.math._rsi import RSI
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, RSI):
        return Raw_mathRSI(x)
    raise Exception('Cannot find suitable overload for Raw('+str(x) +':'+ str(type(x))+')')
