from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.moments.cmv import Variance_Impl
from marketsim import IObservable
@registry.expose(["Statistics", "Var"])
class Var(Function[float], Variance_Impl):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const
        self.source = source if source is not None else const()
        Variance_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable
    }
    def __repr__(self):
        return "\\sigma^2_{cumul}(%(source)s)" % self.__dict__
    
