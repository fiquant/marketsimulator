from marketsim import registry
from marketsim.gen._out.math._moving import Moving
@registry.expose(["-", "Timeframe"])
class Timeframe_mathMoving(object):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math._moving import Moving_IObservableFloatFloat as _math_Moving_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    def __repr__(self):
        return "Moving_{%(timeframe)s}(%(source)s)" % self.__dict__
    
    @property
    def dereference(self):
        return self.x.timeframe
    
def Timeframe(x = None): 
    from marketsim.gen._out.math._moving import Moving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Moving):
        return Timeframe_mathMoving(x)
    raise Exception('Cannot find suitable overload for Timeframe('+str(x) +':'+ str(type(x))+')')
