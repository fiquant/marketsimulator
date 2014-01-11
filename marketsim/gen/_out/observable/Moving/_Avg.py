from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.moments.ma import MA_Impl
from marketsim import IObservable
@registry.expose(["Statistics", "Avg"])
class Avg(Function[float], MA_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._const import const as _const
        self.source = source if source is not None else _const()
        self.timeframe = timeframe if timeframe is not None else 100.0
        MA_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'timeframe' : float
    }
    def __repr__(self):
        return "Avg_{n=%(timeframe)s}(%(source)s)" % self.__dict__
    
