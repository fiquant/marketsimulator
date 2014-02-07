from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim.gen._intrinsic.observable.minmax import Min_Impl
from marketsim import registry
from marketsim import float
@registry.expose(["Statistics", "Min"])
class Min_IFunctionFloatFloat(Observable[float],Min_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import float
        Observable[float].__init__(self)
        self.source = source if source is not None else _constant()
        if isinstance(source, types.IEvent):
            event.subscribe(self.source, self.fire, self)
        self.timeframe = timeframe if timeframe is not None else 100.0
        if isinstance(timeframe, types.IEvent):
            event.subscribe(self.timeframe, self.fire, self)
        rtti.check_fields(self)
        Min_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IFunction[float],
        'timeframe' : float
    }
    def __repr__(self):
        return "Min_{n=%(timeframe)s}(%(source)s)" % self.__dict__
    
def Min(source = None,timeframe = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IFunction[float]):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return Min_IFunctionFloatFloat(source,timeframe)
    raise Exception("Cannot find suitable overload")
