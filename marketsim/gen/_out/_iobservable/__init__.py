from marketsim import meta
from marketsim.gen._out._ievent import IEvent
IObservable = {}
from _iobservableobject import IObservableobject
IObservable[object] = IObservableobject


from _iobservableint import IObservableint
IObservable[int] = IObservableint


from marketsim.gen._out._side import Side
from _iobservableside import IObservableSide
IObservable[Side] = IObservableSide


from _iobservablefloat import IObservablefloat
IObservable[float] = IObservablefloat


from marketsim.gen._out._iorder import IOrder
from _iobservableiorder import IObservableIOrder
IObservable[IOrder] = IObservableIOrder


from _iobservablestr import IObservablestr
IObservable[str] = IObservablestr


from _iobservablebool import IObservablebool
IObservable[bool] = IObservablebool


from marketsim.gen._out._icandlestick import ICandleStick
from _iobservableicandlestick import IObservableICandleStick
IObservable[ICandleStick] = IObservableICandleStick


from marketsim.gen._out._ivolumelevels import IVolumeLevels
from _iobservableivolumelevels import IObservableIVolumeLevels
IObservable[IVolumeLevels] = IObservableIVolumeLevels


