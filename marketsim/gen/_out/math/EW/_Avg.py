from marketsim.gen._intrinsic.moments.ewma import EWMA_Impl
from marketsim import IObservable
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import float
@registry.expose(["Statistics", "Avg"])
class Avg_IObservableFloatFloat(Function[float],EWMA_Impl):
    """ 
    """ 
    def __init__(self, source = None, alpha = None):
        from marketsim.gen._out._const import const_Float as _const
        from marketsim import rtti
        self.source = source if source is not None else _const(1.0)
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
    
def Avg(source = None,alpha = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservable[float]):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return Avg_IObservableFloatFloat(source,alpha)
    raise Exception("Cannot find suitable overload")
