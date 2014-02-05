from marketsim import registry
from marketsim import float
from marketsim import float
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.observable.lagged import Lagged_Impl
from marketsim import IObservable
from marketsim import float
from marketsim import float
@registry.expose(["Basic", "Lagged"])
class Lagged_Optional__IObservable__Float____Optional__Float_(Observable[float],Lagged_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim import float
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const as _const
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        Observable[float].__init__(self)
        self.source = source if source is not None else _const()
        if isinstance(source, types.IEvent):
            event.subscribe(self.source, self.fire, self)
        self.timeframe = timeframe if timeframe is not None else 10.0
        if isinstance(timeframe, types.IEvent):
            event.subscribe(self.timeframe, self.fire, self)
        rtti.check_fields(self)
        Lagged_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'timeframe' : float
    }
    def __repr__(self):
        return "Lagged_{%(timeframe)s}(%(source)s)" % self.__dict__
    
Lagged = Lagged_Optional__IObservable__Float____Optional__Float_
