from marketsim import registry
from marketsim import CandleStick
from marketsim import CandleStick
from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.observable.candlestick import CandleSticks_Impl
from marketsim import IObservable
from marketsim import float
from marketsim import float
@registry.expose(["Basic", "CandleSticks"])
class CandleSticks_Optional__IObservable__Float____Optional__Float_(Observable[CandleStick],CandleSticks_Impl):
    """  open/close/min/max price, its average and standard deviation
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim import CandleStick
        from marketsim import CandleStick
        from marketsim.ops._all import Observable
        from marketsim.gen._out._const import const as _const
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        Observable[CandleStick].__init__(self)
        self.source = source if source is not None else _const()
        if isinstance(source, types.IEvent):
            event.subscribe(self.source, self.fire, self)
        self.timeframe = timeframe if timeframe is not None else 10.0
        if isinstance(timeframe, types.IEvent):
            event.subscribe(self.timeframe, self.fire, self)
        rtti.check_fields(self)
        CandleSticks_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float],
        'timeframe' : float
    }
    def __repr__(self):
        return "Candles_{%(source)s}" % self.__dict__
    
CandleSticks = CandleSticks_Optional__IObservable__Float____Optional__Float_
