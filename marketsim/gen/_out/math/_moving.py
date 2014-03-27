from marketsim import registry
from marketsim.gen._out.math._istatdomain import IStatDomain
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["-", "Moving"])
class Moving_IObservableFloatFloat(IStatDomain):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.source = source if source is not None else deref_opt(_const_Float(0.0))
        self.timeframe = timeframe if timeframe is not None else 100.0
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'timeframe' : float
    }
    def __repr__(self):
        return "Moving_{%(timeframe)s}(%(source)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    

    @property
    def Timeframe(self):
        from marketsim.gen._out.math._timeframe import Timeframe
        return Timeframe(self)
    
    @property
    def RelStdDev(self):
        from marketsim.gen._out.math._relstddev import RelStdDev
        return RelStdDev(self)
    
    @property
    def Var(self):
        from marketsim.gen._out.math._var import Var
        return Var(self)
    
    @property
    def Avg(self):
        from marketsim.gen._out.math._avg import Avg
        return Avg(self)
    
    @property
    def Source(self):
        from marketsim.gen._out.math._source import Source
        return Source(self)
    
    @property
    def StdDev(self):
        from marketsim.gen._out.math._stddev import StdDev
        return StdDev(self)
    
    @property
    def Maximum(self):
        from marketsim.gen._out.math._maximum import Maximum
        return Maximum(self)
    
    @property
    def Minimum(self):
        from marketsim.gen._out.math._minimum import Minimum
        return Minimum(self)
    
    pass
Moving = Moving_IObservableFloatFloat
