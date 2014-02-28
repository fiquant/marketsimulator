from marketsim.gen._out._istatdomain import IStatDomain
class ICumulative(IStatDomain):
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
