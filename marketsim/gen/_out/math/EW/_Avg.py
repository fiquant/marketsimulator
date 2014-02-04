from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.moments.ewma import EWMA_Impl
from marketsim import IObservable
from marketsim import float
from marketsim import float
@registry.expose(["Statistics", "Avg"])
class Avg_Optional__IObservable__Float____Optional__Float_(Function[float], EWMA_Impl):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        self.source = source if source is not None else _const()
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
        EWMA_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'alpha' : float
    }
    def __repr__(self):
        return "Avg_{\\alpha=%(alpha)s}(%(source)s)" % self.__dict__
    
Avg = Avg_Optional__IObservable__Float____Optional__Float_
