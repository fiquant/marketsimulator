from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservableobject import IObservableobject
class IObservablefloat(IEvent, IFunctionfloat):
    _types = []
    _types.append(IObservableobject)
    def DesiredPosition(self, trader = None):
        from marketsim.gen._out.strategy.position._desiredposition import DesiredPosition
        return DesiredPosition(self,trader)
    
    def DownMovements(self, timeframe = None):
        from marketsim.gen._out.math._downmovements import DownMovements
        return DownMovements(self,timeframe)
    
    def Cumulative_MinEpsilon(self, epsilon = None):
        from marketsim.gen._out.math.cumulative._minepsilon import MinEpsilon
        return MinEpsilon(self,epsilon)
    
    def Lagged(self, timeframe = None):
        from marketsim.gen._out.math._lagged import Lagged
        return Lagged(self,timeframe)
    
    @property
    def BreaksAtChanges(self):
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges
        return BreaksAtChanges(self)
    
    def UpMovements(self, timeframe = None):
        from marketsim.gen._out.math._upmovements import UpMovements
        return UpMovements(self,timeframe)
    
    def Moving_Max(self, timeframe = None):
        from marketsim.gen._out.math.moving._max import Max
        return Max(self,timeframe)
    
    def LogReturns(self, timeframe = None):
        from marketsim.gen._out.math._logreturns import LogReturns
        return LogReturns(self,timeframe)
    
    def macd_Signal(self, slow = None,fast = None,timeframe = None,step = None):
        from marketsim.gen._out.math.macd._signal import Signal
        return Signal(self,slow,fast,timeframe,step)
    
    @property
    def Cumulative(self):
        from marketsim.gen._out._cumulative import Cumulative
        return Cumulative(self)
    
    def Moving_Min(self, timeframe = None):
        from marketsim.gen._out.math.moving._min import Min
        return Min(self,timeframe)
    
    def CandleSticks(self, timeframe = None):
        from marketsim.gen._out._candlesticks import CandleSticks
        return CandleSticks(self,timeframe)
    
    def Cumulative_MaxEpsilon(self, epsilon = None):
        from marketsim.gen._out.math.cumulative._maxepsilon import MaxEpsilon
        return MaxEpsilon(self,epsilon)
    
    def EW(self, alpha = None):
        from marketsim.gen._out._ew import EW
        return EW(self,alpha)
    
    def MACD(self, slow = None,fast = None):
        from marketsim.gen._out.math.macd._macd import MACD
        return MACD(self,slow,fast)
    
    def macd_Histogram(self, slow = None,fast = None,timeframe = None,step = None):
        from marketsim.gen._out.math.macd._histogram import Histogram
        return Histogram(self,slow,fast,timeframe,step)
    
    def Moving(self, timeframe = None):
        from marketsim.gen._out._moving import Moving
        return Moving(self,timeframe)
    
    def rsi_Raw(self, timeframe = None,alpha = None):
        from marketsim.gen._out.math.rsi._raw import Raw
        return Raw(self,timeframe,alpha)
    
    @property
    def Link(self):
        from marketsim.gen._out.orderbook._link import Link
        return Link(self)
    
    pass
