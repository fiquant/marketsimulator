# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._intrinsic.observable.minmax_eps import MinEpsilon_Impl
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out.math._cumulative import Cumulative
@registry.expose(["Statistics", "MinEpsilon"])
class MinEpsilon_mathCumulativeFloat(Observablefloat,MinEpsilon_Impl):
    """ **Cumulative minimum of a function with positive tolerance.**
    
    
      It fires updates only if *source* value becomes less than the old value minus *epsilon*
    
    Parameters are:
    
    **x**
    
    **epsilon**
    """ 
    def __init__(self, x = None, epsilon = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.math._cumulative import Cumulative_IObservableFloat as _math_Cumulative_IObservableFloat
        from marketsim import deref_opt
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_Cumulative_IObservableFloat())
        self.epsilon = epsilon if epsilon is not None else deref_opt(_constant_Float(0.01))
        MinEpsilon_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative,
        'epsilon' : IFunctionfloat
    }
    
    
    
    
    
    
    def __repr__(self):
        return "Min_{\\epsilon}(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.x.bind_ex(self._ctx_ex)
        self.epsilon.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.x.reset_ex(generation)
        self.epsilon.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out.math._cumulative import Cumulative
        from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
        rtti.typecheck(Cumulative, self.x)
        rtti.typecheck(IFunctionfloat, self.epsilon)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        self.epsilon.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.registerIn(registry)
                else:
                    v.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        MinEpsilon_Impl.bind_impl(self, ctx)
    
    def reset(self):
        MinEpsilon_Impl.reset(self)
    
def MinEpsilon(x = None,epsilon = None): 
    from marketsim.gen._out.math._cumulative import Cumulative
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Cumulative):
        if epsilon is None or rtti.can_be_casted(epsilon, IFunctionfloat):
            return MinEpsilon_mathCumulativeFloat(x,epsilon)
    raise Exception('Cannot find suitable overload for MinEpsilon('+str(x) +':'+ str(type(x))+','+str(epsilon) +':'+ str(type(epsilon))+')')
