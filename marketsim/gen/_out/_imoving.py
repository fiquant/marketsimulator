from marketsim.gen._out._istatdomain import IStatDomain
class IMoving(IStatDomain):
    @property
    def Timeframe(self):
        from marketsim.gen._out.math.impl._timeframe import Timeframe
        return Timeframe(self)
    
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
    def Maximum(self):
        from marketsim.gen._out.math.impl._maximum import Maximum
        return Maximum(self)
    
    @property
    def Minimum(self):
        from marketsim.gen._out.math.impl._minimum import Minimum
        return Minimum(self)
    
    pass
