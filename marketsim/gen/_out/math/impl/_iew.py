from marketsim.gen._out.math.impl._istatdomain import IStatDomain
class IEW(IStatDomain):
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
    
    @property
    def StdDev(self):
        from marketsim.gen._out.math.impl._stddev import StdDev
        return StdDev(self)
    
    @property
    def Alpha(self):
        from marketsim.gen._out.math.impl._alpha import Alpha
        return Alpha(self)
    
    pass
