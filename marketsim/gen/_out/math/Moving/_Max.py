from marketsim import registry
from marketsim.gen._intrinsic.observable.minmax import Max_Impl
from marketsim import IFunction
from marketsim import float
from marketsim import float
@registry.expose(["Statistics", "Max"])
class Max_Optional__IFunction__Float____Optional__Float_(Max_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        self.source = source if source is not None else _constant()
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
    
Max = Max_Optional__IFunction__Float____Optional__Float_
