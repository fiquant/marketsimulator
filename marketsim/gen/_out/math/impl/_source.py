from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.moments.tmp import Source_Impl
from marketsim.gen._out._istatdomain import IStatDomain
@registry.expose(["Statistics", "Source"])
class Source_IStatDomain(Observablefloat,Source_Impl):
    """ 
    """ 
    def __init__(self, x = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._ew import EW_IObservableFloatFloat as _EW_IObservableFloatFloat
        from marketsim import deref_opt
        from marketsim import rtti
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_EW_IObservableFloatFloat())
        
        rtti.check_fields(self)
        Source_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IStatDomain
    }
    def __repr__(self):
        return "Source(%(x)s)" % self.__dict__
    
def Source(x = None): 
    from marketsim.gen._out._istatdomain import IStatDomain
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IStatDomain):
        return Source_IStatDomain(x)
    raise Exception('Cannot find suitable overload for Source('+str(x) +':'+ str(type(x))+')')
