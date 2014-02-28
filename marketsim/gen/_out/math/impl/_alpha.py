from marketsim import registry
from marketsim.gen._intrinsic.moments.tmp import Alpha_Impl
from marketsim.gen._out._iew import IEW
@registry.expose(["Statistics", "Alpha"])
class Alpha_IEW(Alpha_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out.math.impl._ew import EW_IObservableFloatFloat as _math_impl_EW_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        self.x = x if x is not None else deref_opt(_math_impl_EW_IObservableFloatFloat())
        rtti.check_fields(self)
        Alpha_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IEW
    }
    def __repr__(self):
        return "Alpha(%(x)s)" % self.__dict__
    
def Alpha(x = None): 
    from marketsim.gen._out._iew import IEW
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IEW):
        return Alpha_IEW(x)
    raise Exception('Cannot find suitable overload for Alpha('+str(x) +':'+ str(type(x))+')')
