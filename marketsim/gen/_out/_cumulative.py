from marketsim import registry
from marketsim.gen._out._istatdomain import IStatDomain
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["-", "Cumulative"])
class Cumulative_IObservableFloat(IStatDomain):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.source = source if source is not None else deref_opt(_const_Float(0.0))
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat
    }
    def __repr__(self):
        return "Cumulative(%(source)s)" % self.__dict__
    

    @property
    def RelStdDev(self):
        from marketsim.gen._out.math.impl._relstddev import RelStdDev
        return RelStdDev(self)
    
    @property
    def Var(self):
        from marketsim.gen._out.math.impl._var import Var
        return Var(self)
    
    @property
    def Avg(self):
        from marketsim.gen._out.math.impl._avg import Avg
        return Avg(self)
    
    def MinEpsilon(self, epsilon = None):
        from marketsim.gen._out.math.impl._minepsilon import MinEpsilon
        return MinEpsilon(self,epsilon)
    
    def MaxEpsilon(self, epsilon = None):
        from marketsim.gen._out.math.impl._maxepsilon import MaxEpsilon
        return MaxEpsilon(self,epsilon)
    
    @property
    def StdDev(self):
        from marketsim.gen._out.math.impl._stddev import StdDev
        return StdDev(self)
    
    pass
Cumulative = Cumulative_IObservableFloat
