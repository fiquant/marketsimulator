from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out.math.impl._imoving import IMoving
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_mathimplIMoving(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.math.impl._moving import Moving_IObservableFloatFloat as _math_impl_Moving_IObservableFloatFloat
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_impl_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IMoving
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
        from marketsim.gen._out.math.moving._relstddev import RelStdDev_IObservableFloatFloat as _math_Moving_RelStdDev_IObservableFloatFloat
        from marketsim.gen._out.math.impl._source import Source_mathimplIStatDomain as _math_impl_Source_mathimplIStatDomain
        from marketsim import deref_opt
        from marketsim.gen._out.math.impl._timeframe import Timeframe_mathimplIMoving as _math_impl_Timeframe_mathimplIMoving
        return deref_opt(_math_Moving_RelStdDev_IObservableFloatFloat(deref_opt(_math_impl_Source_mathimplIStatDomain(self.x)),deref_opt(_math_impl_Timeframe_mathimplIMoving(self.x))))
    
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out.math.impl._icumulative import ICumulative
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_mathimplICumulative(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.math.impl._cumulative import Cumulative_IObservableFloat as _math_impl_Cumulative_IObservableFloat
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_impl_Cumulative_IObservableFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : ICumulative
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
        from marketsim.gen._out.math.cumulative._relstddev import RelStdDev_IObservableFloat as _math_Cumulative_RelStdDev_IObservableFloat
        from marketsim.gen._out.math.impl._source import Source_mathimplIStatDomain as _math_impl_Source_mathimplIStatDomain
        from marketsim import deref_opt
        return deref_opt(_math_Cumulative_RelStdDev_IObservableFloat(deref_opt(_math_impl_Source_mathimplIStatDomain(self.x))))
    
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out.math.impl._iew import IEW
from marketsim import context
@registry.expose(["Statistics", "RelStdDev"])
class RelStdDev_mathimplIEW(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.math.impl._ew import EW_IObservableFloatFloat as _math_impl_EW_IObservableFloatFloat
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_impl_EW_IObservableFloatFloat())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IEW
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
        from marketsim.gen._out.math.ew._relstddev import RelStdDev_IObservableFloatFloat as _math_EW_RelStdDev_IObservableFloatFloat
        from marketsim.gen._out.math.impl._source import Source_mathimplIStatDomain as _math_impl_Source_mathimplIStatDomain
        from marketsim import deref_opt
        from marketsim.gen._out.math.impl._alpha import Alpha_mathimplIEW as _math_impl_Alpha_mathimplIEW
        return deref_opt(_math_EW_RelStdDev_IObservableFloatFloat(deref_opt(_math_impl_Source_mathimplIStatDomain(self.x)),deref_opt(_math_impl_Alpha_mathimplIEW(self.x))))
    
def RelStdDev(x = None): 
    from marketsim.gen._out.math.impl._imoving import IMoving
    from marketsim.gen._out.math.impl._icumulative import ICumulative
    from marketsim.gen._out.math.impl._iew import IEW
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IMoving):
        return RelStdDev_mathimplIMoving(x)
    if x is None or rtti.can_be_casted(x, ICumulative):
        return RelStdDev_mathimplICumulative(x)
    if x is None or rtti.can_be_casted(x, IEW):
        return RelStdDev_mathimplIEW(x)
    raise Exception('Cannot find suitable overload for RelStdDev('+str(x) +':'+ str(type(x))+')')
