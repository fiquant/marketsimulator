# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._intrinsic.observable.minmax_eps import MaxEpsilon_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out.math._cumulative import Cumulative
@registry.expose(["Statistics", "MaxEpsilon"])
class MaxEpsilon_mathCumulativeFloat(Observablefloat,MaxEpsilon_Impl):
    """ **Cumulative maximum of a function with positive tolerance.**
    
    
      It fires updates only if *source* value becomes greater than the old value plus *epsilon*
    
    Parameters are:
    
    **x**
    
    **epsilon**
    """ 
    def __init__(self, x = None, epsilon = None):
        from marketsim import rtti
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.math._cumulative import Cumulative_IObservableFloat as _math_Cumulative_IObservableFloat
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_Cumulative_IObservableFloat())
        self.epsilon = epsilon if epsilon is not None else deref_opt(_constant_Float(0.01))
        rtti.check_fields(self)
        MaxEpsilon_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative,
        'epsilon' : IFunctionfloat
    }
    
    
    
    
    
    
    def __repr__(self):
        return "Max_{\\epsilon}(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        if hasattr(self, 'bind_impl'): self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
def MaxEpsilon(x = None,epsilon = None): 
    from marketsim.gen._out.math._cumulative import Cumulative
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Cumulative):
        if epsilon is None or rtti.can_be_casted(epsilon, IFunctionfloat):
            return MaxEpsilon_mathCumulativeFloat(x,epsilon)
    raise Exception('Cannot find suitable overload for MaxEpsilon('+str(x) +':'+ str(type(x))+','+str(epsilon) +':'+ str(type(epsilon))+')')
