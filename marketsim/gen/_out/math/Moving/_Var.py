from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim.gen._intrinsic.moments.mv import MV_Impl
from marketsim import registry
from marketsim import float
@registry.expose(["Statistics", "Var"])
class Var_IObservableFloatFloat(Observable[float],MV_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        from marketsim import float
        Observable[float].__init__(self)
        self.source = source if source is not None else _const_Float(1.0)
        if isinstance(source, types.IEvent):
            event.subscribe(self.source, self.fire, self)
        self.timeframe = timeframe if timeframe is not None else 100.0
        if isinstance(timeframe, types.IEvent):
            event.subscribe(self.timeframe, self.fire, self)
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
