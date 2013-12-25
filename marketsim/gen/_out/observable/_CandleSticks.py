from marketsim import registry
from marketsim.ops._function import Function
from marketsim import CandleStick
from marketsim.gen._intrinsic.observable.candlestick import CandleSticks_Impl
from marketsim import IObservable_Float
@registry.expose(["Basic", "CandleSticks"])
class CandleSticks(Function[CandleStick], CandleSticks_Impl):
    """ 
    """ 
    def __init__(self, source = None, timeframe = None):
        from marketsim.gen._out._const import const
        self.source = source if source is not None else const()
        self.timeframe = timeframe if timeframe is not None else 10.0
        CandleSticks_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable_Float,
        'timeframe' : float
    }
    def __repr__(self):
        return "CandleSticks(%(source)s)" % self.__dict__
    
