from marketsim import registry
from marketsim.gen._intrinsic.observable.minmax import Max_Impl
from marketsim import IFunction
@registry.expose(["Basic", "Max"])
class Max(Max_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._constant import constant
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        self.source = source if source is not None else constant()
        self.timeframe = timeframe if timeframe is not None else 100.0
        Max_Impl.__init__(self)
        if isinstance(source, types.IEvent):
            event.subscribe(self.source, self.fire, self)
        if isinstance(timeframe, types.IEvent):
            event.subscribe(self.timeframe, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IFunction,
        'timeframe' : float
    }
    def __repr__(self):
        return "Max_{n=%(timeframe)s}(%(source)s)" % self.__dict__
    
