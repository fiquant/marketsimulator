from marketsim import registry
from marketsim.gen._out.math._ew import EW
@registry.expose(["-", "Alpha"])
class Alpha_mathEW(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_EW_IObservableFloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : EW
    }
    
    
    def __repr__(self):
        return "EW_{%(alpha)s}(%(source)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        delattr(self, '_processing_ex')
    
    @property
    def dereference(self):
        return self.x.alpha
    
from marketsim import registry
from marketsim.gen._out.math._rsi import RSI
@registry.expose(["-", "Alpha"])
class Alpha_mathRSI(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._rsi import RSI_IObservableFloatFloatFloat as _math_RSI_IObservableFloatFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_RSI_IObservableFloatFloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : RSI
    }
    
    
    def __repr__(self):
        return "RSIRaw_{%(timeframe)s}^{%(alpha)s}(%(source)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bindEx(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        
        delattr(self, '_processing_ex')
    
    @property
    def dereference(self):
        return self.x.alpha
    
def Alpha(x = None): 
    from marketsim.gen._out.math._ew import EW
    from marketsim.gen._out.math._rsi import RSI
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, EW):
        return Alpha_mathEW(x)
    if x is None or rtti.can_be_casted(x, RSI):
        return Alpha_mathRSI(x)
    raise Exception('Cannot find suitable overload for Alpha('+str(x) +':'+ str(type(x))+')')
