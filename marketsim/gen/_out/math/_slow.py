# generated with class generator.python.accessor$Import
from marketsim import registry
from marketsim.gen._out.math._macd import macd
@registry.expose(["-", "Slow"])
class Slow_mathmacd(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._macd import macd_IObservableFloatFloatFloat as _math_macd_IObservableFloatFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_macd_IObservableFloatFloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : macd
    }
    
    
    def __repr__(self):
        return "MACD_{%(fast)s}^{%(slow)s}(%(source)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
    @property
    def dereference(self):
        return self.x.slow
    
def Slow(x = None): 
    from marketsim.gen._out.math._macd import macd
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, macd):
        return Slow_mathmacd(x)
    raise Exception('Cannot find suitable overload for Slow('+str(x) +':'+ str(type(x))+')')
