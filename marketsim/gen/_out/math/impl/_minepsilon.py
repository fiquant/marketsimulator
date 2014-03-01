from marketsim.gen._out._cumulative import Cumulative
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim import context
@registry.expose(["Statistics", "MinEpsilon"])
class MinEpsilon_CumulativeIObservableFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None, epsilon = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim.gen._out._cumulative import Cumulative_IObservableFloat as _Cumulative_IObservableFloat
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_Cumulative_IObservableFloat())
        self.epsilon = epsilon if epsilon is not None else deref_opt(_const_Float(0.01))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative,
        'epsilon' : IObservablefloat
    }
    def __repr__(self):
        return "Min_{\\epsilon}(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out._source import Source_Cumulative as _Source_Cumulative
        from marketsim import deref_opt
        return deref_opt(_math_Cumulative_MinEpsilon_IObservableFloatFloat(deref_opt(_Source_Cumulative(self.x)),self.epsilon))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._cumulative import Cumulative
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim import context
@registry.expose(["Statistics", "MinEpsilon"])
class MinEpsilon_CumulativeFloat(Observablefloat):
    """ 
    """ 
    def __init__(self, x = None, epsilon = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        from marketsim.gen._out._cumulative import Cumulative_IObservableFloat as _Cumulative_IObservableFloat
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_Cumulative_IObservableFloat())
        self.epsilon = epsilon if epsilon is not None else deref_opt(_constant_Float(0.01))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative,
        'epsilon' : IFunctionfloat
    }
    def __repr__(self):
        return "Min_{\\epsilon}(%(x)s)" % self.__dict__
    
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
        from marketsim.gen._out._source import Source_Cumulative as _Source_Cumulative
        from marketsim import deref_opt
        return deref_opt(_math_Cumulative_MinEpsilon_IObservableFloatFloat(deref_opt(_Source_Cumulative(self.x)),self.epsilon))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def MinEpsilon(x = None,epsilon = None): 
    from marketsim.gen._out._cumulative import Cumulative
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Cumulative):
        if epsilon is None or rtti.can_be_casted(epsilon, IObservablefloat):
            return MinEpsilon_CumulativeIObservableFloat(x,epsilon)
    if x is None or rtti.can_be_casted(x, Cumulative):
        if epsilon is None or rtti.can_be_casted(epsilon, IFunctionfloat):
            return MinEpsilon_CumulativeFloat(x,epsilon)
    raise Exception('Cannot find suitable overload for MinEpsilon('+str(x) +':'+ str(type(x))+','+str(epsilon) +':'+ str(type(epsilon))+')')
