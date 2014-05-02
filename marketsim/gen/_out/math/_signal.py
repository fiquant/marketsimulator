# generated with class generator.python.function$Import
from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._out.math._macd import macd
@registry.expose(["MACD", "Signal"])
class Signal_mathmacdFloatFloat(IDifferentiable):
    """ **Moving average convergence/divergence signal**
    
    
    Parameters are:
    
    **x**
    
    **timeframe**
    	 signal period 
    
    **step**
    	 discretization step 
    """ 
    def __init__(self, x = None, timeframe = None, step = None):
        from marketsim.gen._out.math._macd import macd_IObservableFloatFloatFloat as _math_macd_IObservableFloatFloatFloat
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_math_macd_IObservableFloatFloatFloat())
        self.timeframe = timeframe if timeframe is not None else 9.0
        self.step = step if step is not None else 1.0
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
        return "Signal^{%(timeframe)s}_{%(step)s}(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out.math._macd import macd
        rtti.typecheck(macd, self.x)
        rtti.typecheck(float, self.timeframe)
        rtti.typecheck(float, self.step)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.impl.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        
    
    def getImpl(self):
        from marketsim.gen._out.math._value import Value_mathmacd as _math_Value_mathmacd
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim.gen._out.observable._oneverydt import OnEveryDt_FloatFloat as _observable_OnEveryDt_FloatFloat
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim import deref_opt
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
