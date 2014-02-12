from marketsim import IObservable
from marketsim.gen._intrinsic.moments.mv import MV_Impl
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import float
@registry.expose(["Statistics", "Var"])
class Var_IObservableFloatFloat(Function[float],MV_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import rtti
        self.source = source if source is not None else _const_Float(1.0)
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
    from marketsim import IObservable
    from marketsim import float
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IObservable[float]):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return Var_IObservableFloatFloat(source,timeframe)
    raise Exception('Cannot find suitable overload for Var('+str(source)+','+str(timeframe)+')')
