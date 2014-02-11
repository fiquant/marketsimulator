from marketsim.gen._intrinsic.moments.cmv import Variance_Impl
from marketsim import IObservable
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import float
@registry.expose(["Statistics", "Var"])
class Var_IObservableFloat(Function[float],Variance_Impl):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const_Float as _const
        from marketsim import rtti
        self.source = source if source is not None else _const(1.0)
        rtti.check_fields(self)
        Variance_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float]
    }
    def __repr__(self):
        return "\\sigma^2_{cumul}(%(source)s)" % self.__dict__
    
def Var(source = None): 
    from marketsim import IObservable
    from marketsim import float
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservable[float]):
        return Var_IObservableFloat(source)
    raise Exception('Cannot find suitable overload for Var('+str(source)+')')
