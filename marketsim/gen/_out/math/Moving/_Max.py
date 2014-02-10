from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import registry
from marketsim.gen._intrinsic.observable.minmax import Max_Impl
from marketsim import float
@registry.expose(["Statistics", "Max"])
class Max_IFunctionFloatFloat(Observable[float],Max_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim import float
        Observable[float].__init__(self)
        self.source = source if source is not None else _constant(1.0)
        if isinstance(source, types.IEvent):
            event.subscribe(self.source, self.fire, self)
        self.timeframe = timeframe if timeframe is not None else 100.0
        if isinstance(timeframe, types.IEvent):
            event.subscribe(self.timeframe, self.fire, self)
        rtti.check_fields(self)
        Max_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IFunction[float],
        'timeframe' : float
    }
    def __repr__(self):
        return "Max_{n=%(timeframe)s}(%(source)s)" % self.__dict__
    
def Max(source = None,timeframe = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if source is None or rtti.can_be_casted(source, IFunction[float]):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            return Max_IFunctionFloatFloat(source,timeframe)
    raise Exception("Cannot find suitable overload")
