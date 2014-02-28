from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iew import IEW
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev_IEW(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math.impl._ew import EW_IObservableFloatFloat as _math_impl_EW_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_impl_EW_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IEW
    }
    def __repr__(self):
        return "StdDev(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.math.ew._stddev import StdDev_IObservableFloatFloat as _math_EW_StdDev_IObservableFloatFloat
        from marketsim.gen._out.math.impl._source import Source_IStatDomain as _math_impl_Source_IStatDomain
        from marketsim import deref_opt
        from marketsim.gen._out.math.impl._alpha import Alpha_IEW as _math_impl_Alpha_IEW
        return deref_opt(_math_EW_StdDev_IObservableFloatFloat(deref_opt(_math_impl_Source_IStatDomain(self.x)),deref_opt(_math_impl_Alpha_IEW(self.x))))
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._icumulative import ICumulative
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev_ICumulative(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math.impl._cumulative import Cumulative_IObservableFloat as _math_impl_Cumulative_IObservableFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_impl_Cumulative_IObservableFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : ICumulative
    }
    def __repr__(self):
        return "StdDev(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.math.cumulative._stddev import StdDev_IObservableFloat as _math_Cumulative_StdDev_IObservableFloat
        from marketsim.gen._out.math.impl._source import Source_IStatDomain as _math_impl_Source_IStatDomain
        from marketsim import deref_opt
        return deref_opt(_math_Cumulative_StdDev_IObservableFloat(deref_opt(_math_impl_Source_IStatDomain(self.x))))
    
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._imoving import IMoving
from marketsim import context
@registry.expose(["Statistics", "StdDev"])
class StdDev_IMoving(IFunctionfloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math.impl._moving import Moving_IObservableFloatFloat as _math_impl_Moving_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_impl_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IMoving
    }
    def __repr__(self):
        return "StdDev(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.math.moving._stddev import StdDev_IObservableFloatFloat as _math_Moving_StdDev_IObservableFloatFloat
        from marketsim.gen._out.math.impl._source import Source_IStatDomain as _math_impl_Source_IStatDomain
        from marketsim import deref_opt
        from marketsim.gen._out.math.impl._timeframe import Timeframe_IMoving as _math_impl_Timeframe_IMoving
        return deref_opt(_math_Moving_StdDev_IObservableFloatFloat(deref_opt(_math_impl_Source_IStatDomain(self.x)),deref_opt(_math_impl_Timeframe_IMoving(self.x))))
    
def StdDev(x = None): 
    from marketsim.gen._out._iew import IEW
    from marketsim.gen._out._icumulative import ICumulative
    from marketsim.gen._out._imoving import IMoving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IEW):
        return StdDev_IEW(x)
    if x is None or rtti.can_be_casted(x, ICumulative):
        return StdDev_ICumulative(x)
    if x is None or rtti.can_be_casted(x, IMoving):
        return StdDev_IMoving(x)
    raise Exception('Cannot find suitable overload for StdDev('+str(x) +':'+ str(type(x))+')')
