# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablebool import Observablebool
from marketsim.gen._intrinsic._constant import False_Impl
@registry.expose(["Basic", "observableFalse"])
class observableFalse_(Observablebool,False_Impl):
    """ **Trivial observable always returning *False***
    
    
    Parameters are:
    """ 
    def __init__(self):
        from marketsim.gen._out._observable._observablebool import Observablebool
        from marketsim import rtti
        Observablebool.__init__(self)
        
        rtti.check_fields(self)
        False_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "False" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if getattr(self, '_processing_ex', False):
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
        
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        self._processing_ex = False
    
def observableFalse(): 
    from marketsim import rtti
    return observableFalse_()
    raise Exception('Cannot find suitable overload for observableFalse('++')')
