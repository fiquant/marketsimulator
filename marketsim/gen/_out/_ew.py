from marketsim import registry
from marketsim.gen._out._istatdomain import IStatDomain
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["-", "EW"])
class EW_IObservableFloatFloat(IStatDomain):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim import rtti
        self.source = source if source is not None else deref_opt(_const_Float(0.0))
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservablefloat,
        'alpha' : float
    }
    def __repr__(self):
        return "EW_{%(alpha)s}(%(source)s)" % self.__dict__
    

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
    def Source(self):
        from marketsim.gen._out._source import Source
        return Source(self)
    
    @property
    def StdDev(self):
        from marketsim.gen._out.math.impl._stddev import StdDev
        return StdDev(self)
    
    @property
    def Alpha(self):
        from marketsim.gen._out._alpha import Alpha
        return Alpha(self)
    
    pass
EW = EW_IObservableFloatFloat
