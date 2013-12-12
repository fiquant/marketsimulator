from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.moments.ewmv import EWMV_Impl
from marketsim import IObservable
from marketsim import float
@registry.expose(["Statistics", "Var"])
class Var(Function[float], EWMV_Impl):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        from marketsim.gen._out._const import const
        self.source = source if source is not None else const()
        self.alpha = alpha if alpha is not None else 0.015
        EWMV_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable,
        'alpha' : float
    }
    def __repr__(self):
        return "\\sigma^2^{\\alpha=%(alpha)s}_{%(source)s}" % self.__dict__
    
