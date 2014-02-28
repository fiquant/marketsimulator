from marketsim import registry
from marketsim.gen._intrinsic.moments.tmp import Timeframe_Impl
from marketsim.gen._out._moving import Moving
@registry.expose(["Statistics", "Timeframe"])
class Timeframe_Moving(Timeframe_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._moving import Moving_IObservableFloatFloat as _Moving_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        Timeframe_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    def __repr__(self):
        return "Timeframe(%(x)s)" % self.__dict__
    
def Timeframe(x = None): 
    from marketsim.gen._out._moving import Moving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Moving):
        return Timeframe_Moving(x)
    raise Exception('Cannot find suitable overload for Timeframe('+str(x) +':'+ str(type(x))+')')
