# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.observable.minmax import Max_Impl
from marketsim.gen._out.math._moving import Moving
@registry.expose(["Statistics", "Maximum"])
class Maximum_mathMoving(Observablefloat,Max_Impl):
    """ **Running maximum of a function**
    
    
    Parameters are:
    
    **x**
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.math._moving import Moving_IObservableFloatFloat as _math_Moving_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        Max_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    
    
    
    def __repr__(self):
        return "Maximum(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self._ctx_ex)
                else:
                    v.bind_ex(self._ctx_ex)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def Maximum(x = None): 
    from marketsim.gen._out.math._moving import Moving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Moving):
        return Maximum_mathMoving(x)
    raise Exception('Cannot find suitable overload for Maximum('+str(x) +':'+ str(type(x))+')')
