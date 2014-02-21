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
    def sideprice_FloatingPrice(self, proto = None):
        from marketsim.gen._out.order._curried._sideprice_floatingprice import sideprice_FloatingPrice
        return sideprice_FloatingPrice(self,proto)
    
    def Min(self, timeframe = None):
        from marketsim.gen._out.math.Moving._min import Min
        return Min(self,timeframe)
    
    def Histogram(self, slow = None,fast = None,timeframe = None,step = None):
        from marketsim.gen._out.math.macd._histogram import Histogram
        return Histogram(self,slow,fast,timeframe,step)
    
    def Signal(self, slow = None,fast = None,timeframe = None,step = None):
        from marketsim.gen._out.math.macd._signal import Signal
        return Signal(self,slow,fast,timeframe,step)
    
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
    
    def Max(self, timeframe = None):
        from marketsim.gen._out.math.Moving._max import Max
        return Max(self,timeframe)
    
    def UpMovements(self, timeframe = None):
        from marketsim.gen._out.math._upmovements import UpMovements
        return UpMovements(self,timeframe)
    
    def LogReturns(self, timeframe = None):
        from marketsim.gen._out.math._logreturns import LogReturns
        return LogReturns(self,timeframe)
    
    def volume_FloatingPrice(self, proto = None):
        from marketsim.gen._out.order._curried._volume_floatingprice import volume_FloatingPrice
        return volume_FloatingPrice(self,proto)
    
    def side_price_FloatingPrice(self, proto = None):
        from marketsim.gen._out.order._curried._side_price_floatingprice import side_price_FloatingPrice
        return side_price_FloatingPrice(self,proto)
    
    def side_FloatingPrice(self, proto = None):
        from marketsim.gen._out.order._curried._side_floatingprice import side_FloatingPrice
        return side_FloatingPrice(self,proto)
    
    def volume_price_FloatingPrice(self, proto = None):
        from marketsim.gen._out.order._curried._volume_price_floatingprice import volume_price_FloatingPrice
        return volume_price_FloatingPrice(self,proto)
    
    def price_FloatingPrice(self, proto = None):
        from marketsim.gen._out.order._curried._price_floatingprice import price_FloatingPrice
        return price_FloatingPrice(self,proto)
    
    def MinEpsilon(self, epsilon = None):
        from marketsim.gen._out.math.Cumulative._minepsilon import MinEpsilon
        return MinEpsilon(self,epsilon)
    
    def sidevolume_FloatingPrice(self, proto = None):
        from marketsim.gen._out.order._curried._sidevolume_floatingprice import sidevolume_FloatingPrice
        return sidevolume_FloatingPrice(self,proto)
    
    def MaxEpsilon(self, epsilon = None):
        from marketsim.gen._out.math.Cumulative._maxepsilon import MaxEpsilon
        return MaxEpsilon(self,epsilon)
    
    def CandleSticks(self, timeframe = None):
        from marketsim.gen._out._candlesticks import CandleSticks
        return CandleSticks(self,timeframe)
    
    def FloatingPrice(self, proto = None):
        from marketsim.gen._out.order._floatingprice import FloatingPrice
        return FloatingPrice(self,proto)
    
    def sidevolume_price_FloatingPrice(self, proto = None):
        from marketsim.gen._out.order._curried._sidevolume_price_floatingprice import sidevolume_price_FloatingPrice
        return sidevolume_price_FloatingPrice(self,proto)
    
    def Raw(self, timeframe = None,alpha = None):
        from marketsim.gen._out.math.rsi._raw import Raw
        return Raw(self,timeframe,alpha)
    
    def MACD(self, slow = None,fast = None):
        from marketsim.gen._out.math.macd._macd import MACD
        return MACD(self,slow,fast)
    
    @property
    def O(self):
        from marketsim.gen._out._test.in1.in2._o import O
        return O(self)
    
    @property
    def Link(self):
        from marketsim.gen._out.orderbook._link import Link
        return Link(self)
    
    pass


IObservable[float] = IObservablefloat


from marketsim.gen._out._ifunction import IFunctionIOrder
from marketsim.gen._out._iorder import IOrder
class IObservableIOrder(IEvent, IFunctionIOrder):
    @property
    def ImmediateOrCancel(self):
        from marketsim.gen._out.order._immediateorcancel import ImmediateOrCancel
        return ImmediateOrCancel(self)
    
    def Generic(self, eventGen = None):
        from marketsim.gen._out.strategy._generic import Generic
        return Generic(self,eventGen)
    
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


