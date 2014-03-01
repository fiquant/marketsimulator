from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._ew import EW
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_EW(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._ew import EW_IObservableFloatFloat as _EW_IObservableFloatFloat
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_EW_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : EW
    }
    def __repr__(self):
        return "RelStdDev(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out.math._avg import Avg_EW as _math_Avg_EW
        from marketsim.gen._out._source import Source_EW as _Source_EW
        from marketsim import deref_opt
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatFloat as _ops_Sub_IObservableFloatFloat
        from marketsim.gen._out.math._stddev import StdDev_EW as _math_StdDev_EW
        return deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_ops_Sub_IObservableFloatFloat(deref_opt(_Source_EW(self.x)),deref_opt(_math_Avg_EW(self.x)))),deref_opt(_math_StdDev_EW(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._cumulative import Cumulative
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_Cumulative(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._cumulative import Cumulative_IObservableFloat as _Cumulative_IObservableFloat
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_Cumulative_IObservableFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative
    }
    def __repr__(self):
        return "RelStdDev(%(x)s)" % self.__dict__
    
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
        from marketsim import deref_opt
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out._source import Source_Cumulative as _Source_Cumulative
        from marketsim.gen._out.math._stddev import StdDev_Cumulative as _math_StdDev_Cumulative
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatFloat as _ops_Sub_IObservableFloatFloat
        from marketsim.gen._out.math._avg import Avg_Cumulative as _math_Avg_Cumulative
        return deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_ops_Sub_IObservableFloatFloat(deref_opt(_Source_Cumulative(self.x)),deref_opt(_math_Avg_Cumulative(self.x)))),deref_opt(_math_StdDev_Cumulative(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._moving import Moving
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_Moving(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._moving import Moving_IObservableFloatFloat as _Moving_IObservableFloatFloat
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    def __repr__(self):
        return "RelStdDev(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out._source import Source_Moving as _Source_Moving
        from marketsim import deref_opt
        from marketsim.gen._out.ops._div import Div_IObservableFloatFloat as _ops_Div_IObservableFloatFloat
        from marketsim.gen._out.math._avg import Avg_Moving as _math_Avg_Moving
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatFloat as _ops_Sub_IObservableFloatFloat
        from marketsim.gen._out.math._stddev import StdDev_Moving as _math_StdDev_Moving
        return deref_opt(_ops_Div_IObservableFloatFloat(deref_opt(_ops_Sub_IObservableFloatFloat(deref_opt(_Source_Moving(self.x)),deref_opt(_math_Avg_Moving(self.x)))),deref_opt(_math_StdDev_Moving(self.x))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def RelStdDev(x = None): 
    from marketsim.gen._out._ew import EW
    from marketsim.gen._out._cumulative import Cumulative
    from marketsim.gen._out._moving import Moving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, EW):
        return RelStdDev_EW(x)
    if x is None or rtti.can_be_casted(x, Cumulative):
        return RelStdDev_Cumulative(x)
    if x is None or rtti.can_be_casted(x, Moving):
        return RelStdDev_Moving(x)
    raise Exception('Cannot find suitable overload for RelStdDev('+str(x) +':'+ str(type(x))+')')
