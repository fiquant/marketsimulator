from marketsim import registry
from marketsim.gen._out.math.macd._macd import macd
@registry.expose(["-", "X"])
class X_mathmacdmacd(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math.macd._macd import macd_IObservableFloatFloatFloat as _math_macd_macd_IObservableFloatFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_macd_macd_IObservableFloatFloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : macd
    }
    def __repr__(self):
        return "X(%(x)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.x
    
def X(x = None): 
    from marketsim.gen._out.math.macd._macd import macd
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, macd):
        return X_mathmacdmacd(x)
    raise Exception('Cannot find suitable overload for X('+str(x) +':'+ str(type(x))+')')
