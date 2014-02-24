from marketsim import meta
from marketsim.gen._out._ievent import IEvent
IObservable = {}
from marketsim.gen._out._ifunction import IFunctionobject
class IObservableobject(IEvent, IFunctionobject):
    def TimeSerie(self, graph = None,_digitsToShow = None,_smooth = None):
        from marketsim.gen._out._timeserie import TimeSerie
        return TimeSerie(self,graph,_digitsToShow,_smooth)
    
    pass


IObservable[object] = IObservableobject


from marketsim.gen._out._ifunction import IFunctionint
class IObservableint(IEvent, IFunctionint):
    pass


IObservable[int] = IObservableint


from marketsim.gen._out._ifunction import IFunctionSide
from marketsim.gen._out._side import Side
class IObservableSide(IEvent, IFunctionSide):
    pass


IObservable[Side] = IObservableSide


from marketsim.gen._out._ifunction import IFunctionfloat
class IObservablefloat(IEvent, IFunctionfloat):
    def Moving_Avg(self, timeframe = None):
        from marketsim.gen._out.math.Moving._avg import Avg
        return Avg(self,timeframe)
    
    @property
    def Cumulative_Var(self):
        from marketsim.gen._out.math.Cumulative._var import Var
        return Var(self)
    
    def DownMovements(self, timeframe = None):
        from marketsim.gen._out.math._downmovements import DownMovements
        return DownMovements(self,timeframe)
    
    def EW_Var(self, alpha = None):
        from marketsim.gen._out.math.EW._var import Var
        return Var(self,alpha)
    
    def Cumulative_MinEpsilon(self, epsilon = None):
        from marketsim.gen._out.math.Cumulative._minepsilon import MinEpsilon
        return MinEpsilon(self,epsilon)
    
    def Lagged(self, timeframe = None):
        from marketsim.gen._out.math._lagged import Lagged
        return Lagged(self,timeframe)
    
    @property
    def Cumulative_Avg(self):
        from marketsim.gen._out.math.Cumulative._avg import Avg
        return Avg(self)
    
    @property
    def BreaksAtChanges(self):
        from marketsim.gen._out.observable._breaksatchanges import BreaksAtChanges
        return BreaksAtChanges(self)
    
    def UpMovements(self, timeframe = None):
        from marketsim.gen._out.math._upmovements import UpMovements
        return UpMovements(self,timeframe)
    
    def Moving_Max(self, timeframe = None):
        from marketsim.gen._out.math.Moving._max import Max
        return Max(self,timeframe)
    
    def LogReturns(self, timeframe = None):
        from marketsim.gen._out.math._logreturns import LogReturns
        return LogReturns(self,timeframe)
    
    def macd_Signal(self, slow = None,fast = None,timeframe = None,step = None):
        from marketsim.gen._out.math.macd._signal import Signal
        return Signal(self,slow,fast,timeframe,step)
    
    @property
    def Cumulative_StdDev(self):
        from marketsim.gen._out.math.Cumulative._stddev import StdDev
        return StdDev(self)
    
    def EW_RelStdDev(self, alpha = None):
        from marketsim.gen._out.math.EW._relstddev import RelStdDev
        return RelStdDev(self,alpha)
    
    def EW_StdDev(self, alpha = None):
        from marketsim.gen._out.math.EW._stddev import StdDev
        return StdDev(self,alpha)
    
    def Moving_Min(self, timeframe = None):
        from marketsim.gen._out.math.Moving._min import Min
        return Min(self,timeframe)
    
    def Moving_StdDev(self, timeframe = None):
        from marketsim.gen._out.math.Moving._stddev import StdDev
        return StdDev(self,timeframe)
    
    def Moving_Var(self, timeframe = None):
        from marketsim.gen._out.math.Moving._var import Var
        return Var(self,timeframe)
    
    def Moving_RelStdDev(self, timeframe = None):
        from marketsim.gen._out.math.Moving._relstddev import RelStdDev
        return RelStdDev(self,timeframe)
    
    def CandleSticks(self, timeframe = None):
        from marketsim.gen._out._candlesticks import CandleSticks
        return CandleSticks(self,timeframe)
    
    def EW_Avg(self, alpha = None):
        from marketsim.gen._out.math.EW._avg import Avg
        return Avg(self,alpha)
    
    def Cumulative_MaxEpsilon(self, epsilon = None):
        from marketsim.gen._out.math.Cumulative._maxepsilon import MaxEpsilon
        return MaxEpsilon(self,epsilon)
    
    def Raw(self, timeframe = None,alpha = None):
        from marketsim.gen._out.math.rsi._raw import Raw
        return Raw(self,timeframe,alpha)
    
    def MACD(self, slow = None,fast = None):
        from marketsim.gen._out.math.macd._macd import MACD
        return MACD(self,slow,fast)
    
    def macd_Histogram(self, slow = None,fast = None,timeframe = None,step = None):
        from marketsim.gen._out.math.macd._histogram import Histogram
        return Histogram(self,slow,fast,timeframe,step)
    
    @property
    def Cumulative_RelStdDev(self):
        from marketsim.gen._out.math.Cumulative._relstddev import RelStdDev
        return RelStdDev(self)
    
    @property
    def Link(self):
        from marketsim.gen._out.orderbook._link import Link
        return Link(self)
    
    pass


IObservable[float] = IObservablefloat


from marketsim.gen._out._ifunction import IFunctionIOrder
from marketsim.gen._out._iorder import IOrder
class IObservableIOrder(IEvent, IFunctionIOrder):
    pass


IObservable[IOrder] = IObservableIOrder


from marketsim.gen._out._ifunction import IFunctionstr
class IObservablestr(IEvent, IFunctionstr):
    pass


IObservable[str] = IObservablestr


from marketsim.gen._out._ifunction import IFunctionbool
class IObservablebool(IEvent, IFunctionbool):
    pass


IObservable[bool] = IObservablebool


from marketsim.gen._out._ifunction import IFunctionICandleStick
from marketsim.gen._out._icandlestick import ICandleStick
class IObservableICandleStick(IEvent, IFunctionICandleStick):
    pass


IObservable[ICandleStick] = IObservableICandleStick


from marketsim.gen._out._ifunction import IFunctionIVolumeLevels
from marketsim.gen._out._ivolumelevels import IVolumeLevels
class IObservableIVolumeLevels(IEvent, IFunctionIVolumeLevels):
    pass


IObservable[IVolumeLevels] = IObservableIVolumeLevels


