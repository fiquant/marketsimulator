from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.moments.mv import MV_Impl
from marketsim import IObservable_Float
@registry.expose(["Statistics", "Var"])
class Var(Function[float], MV_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._const import const
        self.source = source if source is not None else const()
        self.timeframe = timeframe if timeframe is not None else 100.0
        MV_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable_Float,
        'timeframe' : float
    }
    def __repr__(self):
        return "\\sigma^2_{n=%(timeframe)s}(%(source)s)" % self.__dict__
    
