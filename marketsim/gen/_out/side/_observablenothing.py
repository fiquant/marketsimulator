# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._side import Side
from marketsim.gen._out._observable._observableside import ObservableSide
from marketsim.gen._intrinsic.side import None_Impl
@registry.expose(["Side", "observableNothing"])
class observableNothing_(ObservableSide,None_Impl):
    """ **Observable always equal to None of type Side**
    
    
    Parameters are:
    """ 
    def __init__(self):
        from marketsim.gen._out._side import Side
        from marketsim.gen._out._observable._observableside import ObservableSide
        from marketsim import rtti
        ObservableSide.__init__(self)
        
        rtti.check_fields(self)
        None_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    
    def __repr__(self):
        return "observableNothing" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
    
def observableNothing(): 
    from marketsim import rtti
    return observableNothing_()
    raise Exception('Cannot find suitable overload for observableNothing('++')')
