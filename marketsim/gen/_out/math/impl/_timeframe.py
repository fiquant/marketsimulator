from marketsim import registry
from marketsim.gen._intrinsic.moments.tmp import Timeframe_Impl
from marketsim.gen._out.math.impl._imoving import IMoving
@registry.expose(["Statistics", "Timeframe"])
class Timeframe_mathimplIMoving(Timeframe_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math.impl._moving import Moving_IObservableFloatFloat as _math_impl_Moving_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_impl_Moving_IObservableFloatFloat())
        rtti.check_fields(self)
        Timeframe_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IMoving
    }
    def __repr__(self):
        return "Timeframe(%(x)s)" % self.__dict__
    
def Timeframe(x = None): 
    from marketsim.gen._out.math.impl._imoving import IMoving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IMoving):
        return Timeframe_mathimplIMoving(x)
    raise Exception('Cannot find suitable overload for Timeframe('+str(x) +':'+ str(type(x))+')')
