from marketsim import meta
from marketsim.gen._out._ievent import IEvent
IObservable = {}
from marketsim.gen._out._ifunction import IFunctionobject
class IObservableobject(IEvent, IFunctionobject):
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
    pass


IObservable[float] = IObservablefloat


from marketsim.gen._out._ifunction import IFunctionstr
class IObservablestr(IEvent, IFunctionstr):
    pass


IObservable[str] = IObservablestr


from marketsim.gen._out._ifunction import IFunctionIOrder
from marketsim.gen._out._iorder import IOrder
class IObservableIOrder(IEvent, IFunctionIOrder):
    pass


IObservable[IOrder] = IObservableIOrder


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


