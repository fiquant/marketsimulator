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
    
    def LogReturns(self, timeframe = None):
        from marketsim.gen._out.math._logreturns import LogReturns
        return LogReturns(self,timeframe)
    
    @property
    def Cumulative(self):
        from marketsim.gen._out.math._cumulative import Cumulative
        return Cumulative(self)
    
    def macd(self, slow = None,fast = None):
        from marketsim.gen._out.math._macd import macd
        return macd(self,slow,fast)
    
    def CandleSticks(self, timeframe = None):
        from marketsim.gen._out._candlesticks import CandleSticks
        return CandleSticks(self,timeframe)
    
    def EW(self, alpha = None):
        from marketsim.gen._out.math._ew import EW
        return EW(self,alpha)
    
    def Moving(self, timeframe = None):
        from marketsim.gen._out.math._moving import Moving
        return Moving(self,timeframe)
    
    def rsi_Raw(self, timeframe = None,alpha = None):
        from marketsim.gen._out.math.rsi._raw import Raw
        return Raw(self,timeframe,alpha)
    
    @property
    def Link(self):
        from marketsim.gen._out.orderbook._link import Link
        return Link(self)
    
    pass
