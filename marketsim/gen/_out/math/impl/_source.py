from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.moments.tmp import Source_Impl
from marketsim.gen._out.math.impl._istatdomain import IStatDomain
@registry.expose(["Statistics", "source"])
class source_mathimplIStatDomain(Observablefloat,Source_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out.math.impl._ew import EW_IObservableFloatFloat as _math_impl_EW_IObservableFloatFloat
        from marketsim import call
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.x = x if x is not None else call(_math_impl_EW_IObservableFloatFloat,)
        
        rtti.check_fields(self)
        Source_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IStatDomain
    }
    def __repr__(self):
        return "source(%(x)s)" % self.__dict__
    
def source(x = None): 
    from marketsim.gen._out.math.impl._istatdomain import IStatDomain
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IStatDomain):
        return source_mathimplIStatDomain(x)
    raise Exception('Cannot find suitable overload for source('+str(x) +':'+ str(type(x))+')')
