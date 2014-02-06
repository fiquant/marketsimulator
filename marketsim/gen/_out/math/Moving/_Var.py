from marketsim import IObservable
from marketsim.gen._intrinsic.moments.mv import MV_Impl
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import float
@registry.expose(["Statistics", "Var"])
class Var_Optional__IObservable__Float____Optional__Float_(Function[float],MV_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        self.source = source if source is not None else _const()
        self.timeframe = timeframe if timeframe is not None else 100.0
        rtti.check_fields(self)
        MV_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'timeframe' : float
    }
    def __repr__(self):
        return "\\sigma^2_{n=%(timeframe)s}(%(source)s)" % self.__dict__
    
def Var(source = None,timeframe = None): 
    return Var_Optional__IObservable__Float____Optional__Float_(source,timeframe)
