from marketsim import registry
from marketsim.gen._intrinsic.moments.tmp import Timeframe_Impl
from marketsim.gen._out.math.impl._imoving import IMoving
@registry.expose(["Statistics", "timeframe"])
class timeframe_mathimplIMoving(float,Timeframe_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math.impl._moving import Moving_IObservableFloatFloat as _math_impl_Moving_IObservableFloatFloat
        from marketsim import call
        from marketsim import rtti
        self.x = x if x is not None else call(_math_impl_Moving_IObservableFloatFloat,)
        rtti.check_fields(self)
        Timeframe_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IMoving
    }
    def __repr__(self):
        return "timeframe(%(x)s)" % self.__dict__
    
def timeframe(x = None): 
    from marketsim.gen._out.math.impl._imoving import IMoving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IMoving):
        return timeframe_mathimplIMoving(x)
    raise Exception('Cannot find suitable overload for timeframe('+str(x) +':'+ str(type(x))+')')
