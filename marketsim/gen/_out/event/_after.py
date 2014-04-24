# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._intrinsic.event import After_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Event", "After"])
class After_Float(IEvent,After_Impl):
    """ **Event that once at *delay***
    
    
    Parameters are:
    
    **delay**
    	 when the event should be fired 
    """ 
    def __init__(self, delay = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.delay = delay if delay is not None else deref_opt(_constant_Float(10.0))
        rtti.check_fields(self)
        After_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'delay' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "After(%(delay)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
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
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        self.delay.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def After(delay = None): 
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if delay is None or rtti.can_be_casted(delay, IFunctionfloat):
        return After_Float(delay)
    raise Exception('Cannot find suitable overload for After('+str(delay) +':'+ str(type(delay))+')')
