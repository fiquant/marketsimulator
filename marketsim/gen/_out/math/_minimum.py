from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.observable.minmax import Min_Impl
from marketsim.gen._out.math._moving import Moving
@registry.expose(["Statistics", "Minimum"])
class Minimum_mathMoving(Observablefloat,Min_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.math._moving import Moving_IObservableFloatFloat as _math_Moving_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_Moving_IObservableFloatFloat())
        
        rtti.check_fields(self)
        Min_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Moving
    }
    def __repr__(self):
        return "Minimum(%(x)s)" % self.__dict__
    
def Minimum(x = None): 
    from marketsim.gen._out.math._moving import Moving
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Moving):
        return Minimum_mathMoving(x)
    raise Exception('Cannot find suitable overload for Minimum('+str(x) +':'+ str(type(x))+')')
