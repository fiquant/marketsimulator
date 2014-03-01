from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._out._ew import EW
from marketsim import context
@registry.expose(["Statistics", "Avg"])
class Avg_EW(IDifferentiable):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._ew import EW_IObservableFloatFloat as _EW_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_EW_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : EW
    }
    def __repr__(self):
        return "Avg(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out._source import Source_EW as _Source_EW
        from marketsim import deref_opt
        from marketsim.gen._out._alpha import Alpha_EW as _Alpha_EW
        return deref_opt(_math_EW_Avg_IObservableFloatFloat(deref_opt(_Source_EW(self.x)),deref_opt(_Alpha_EW(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._out._cumulative import Cumulative
from marketsim import context
@registry.expose(["Statistics", "Avg"])
class Avg_Cumulative(IDifferentiable):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._cumulative import Cumulative_IObservableFloat as _Cumulative_IObservableFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_Cumulative_IObservableFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative
    }
    def __repr__(self):
        return "Avg(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.math.cumulative._avg import Avg_IObservableFloat as _math_Cumulative_Avg_IObservableFloat
        from marketsim.gen._out._source import Source_Cumulative as _Source_Cumulative
        from marketsim import deref_opt
        return deref_opt(_math_Cumulative_Avg_IObservableFloat(deref_opt(_Source_Cumulative(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._out._moving import Moving
from marketsim import context
@registry.expose(["Statistics", "Avg"])
class Avg_Moving(IDifferentiable):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._moving import Moving_IObservableFloatFloat as _Moving_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    def __repr__(self):
        return "Avg(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.math.moving._avg import Avg_IObservableFloatFloat as _math_Moving_Avg_IObservableFloatFloat
        from marketsim.gen._out._source import Source_Moving as _Source_Moving
        from marketsim import deref_opt
        from marketsim.gen._out._timeframe import Timeframe_Moving as _Timeframe_Moving
        return deref_opt(_math_Moving_Avg_IObservableFloatFloat(deref_opt(_Source_Moving(self.x)),deref_opt(_Timeframe_Moving(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def Avg(x = None): 
    from marketsim.gen._out._ew import EW
    from marketsim.gen._out._cumulative import Cumulative
    from marketsim.gen._out._moving import Moving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, EW):
        return Avg_EW(x)
    if x is None or rtti.can_be_casted(x, Cumulative):
        return Avg_Cumulative(x)
    if x is None or rtti.can_be_casted(x, Moving):
        return Avg_Moving(x)
    raise Exception('Cannot find suitable overload for Avg('+str(x) +':'+ str(type(x))+')')
