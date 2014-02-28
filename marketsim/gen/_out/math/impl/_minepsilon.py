from marketsim.gen._out._icumulative import ICumulative
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim import context
@registry.expose(["Statistics", "MinEpsilon"])
class MinEpsilon_ICumulativeIObservableFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None, epsilon = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.math.impl._cumulative import Cumulative_IObservableFloat as _math_impl_Cumulative_IObservableFloat
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_impl_Cumulative_IObservableFloat())
        self.epsilon = epsilon if epsilon is not None else deref_opt(_const_Float(0.01))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : ICumulative,
        'epsilon' : IObservablefloat
    }
    def __repr__(self):
        return "MinEpsilon(%(x)s, %(epsilon)s)" % self.__dict__
    
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
        from marketsim.gen._out.math.cumulative._minepsilon import MinEpsilon_IObservableFloatFloat as _math_Cumulative_MinEpsilon_IObservableFloatFloat
        from marketsim.gen._out.math.impl._source import Source_IStatDomain as _math_impl_Source_IStatDomain
        from marketsim import deref_opt
        return deref_opt(_math_Cumulative_MinEpsilon_IObservableFloatFloat(deref_opt(_math_impl_Source_IStatDomain(self.x)),self.epsilon))
    
from marketsim.gen._out._icumulative import ICumulative
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim import context
@registry.expose(["Statistics", "MinEpsilon"])
class MinEpsilon_ICumulativeFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None, epsilon = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.math.impl._cumulative import Cumulative_IObservableFloat as _math_impl_Cumulative_IObservableFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_impl_Cumulative_IObservableFloat())
        self.epsilon = epsilon if epsilon is not None else deref_opt(_constant_Float(0.01))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : ICumulative,
        'epsilon' : IFunctionfloat
    }
    def __repr__(self):
        return "MinEpsilon(%(x)s, %(epsilon)s)" % self.__dict__
    
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
        from marketsim.gen._out.math.cumulative._minepsilon import MinEpsilon_IObservableFloatFloat as _math_Cumulative_MinEpsilon_IObservableFloatFloat
        from marketsim.gen._out.math.impl._source import Source_IStatDomain as _math_impl_Source_IStatDomain
        from marketsim import deref_opt
        return deref_opt(_math_Cumulative_MinEpsilon_IObservableFloatFloat(deref_opt(_math_impl_Source_IStatDomain(self.x)),self.epsilon))
    
def MinEpsilon(x = None,epsilon = None): 
    from marketsim.gen._out._icumulative import ICumulative
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, ICumulative):
        if epsilon is None or rtti.can_be_casted(epsilon, IObservablefloat):
            return MinEpsilon_ICumulativeIObservableFloat(x,epsilon)
    if x is None or rtti.can_be_casted(x, ICumulative):
        if epsilon is None or rtti.can_be_casted(epsilon, IFunctionfloat):
            return MinEpsilon_ICumulativeFloat(x,epsilon)
    raise Exception('Cannot find suitable overload for MinEpsilon('+str(x) +':'+ str(type(x))+','+str(epsilon) +':'+ str(type(epsilon))+')')
