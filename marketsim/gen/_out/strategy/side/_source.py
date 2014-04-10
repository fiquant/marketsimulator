# generated with class generator.python.accessor$Import
from marketsim import registry
from marketsim.gen._out.strategy.side._signal import Signal
@registry.expose(["-", "Source"])
class Source_strategysideSignal(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_strategy_side_Signal_FloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Signal
    }
    
    
    def __repr__(self):
        return "Source(%(x)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
    @property
    def dereference(self):
        return self.x.source
    
def Source(x = None): 
    from marketsim.gen._out.strategy.side._signal import Signal
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Signal):
        return Source_strategysideSignal(x)
    raise Exception('Cannot find suitable overload for Source('+str(x) +':'+ str(type(x))+')')
