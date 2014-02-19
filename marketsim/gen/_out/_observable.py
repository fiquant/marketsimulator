from marketsim.event import Conditional_Impl
Observable = {}
from marketsim.gen._out._iobservable import IObservableint
class Observableint(Conditional_Impl, IObservableint):
    pass


Observable[int] = Observableint


from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
class ObservableSide(Conditional_Impl, IObservableSide):
    pass


Observable[Side] = ObservableSide


from marketsim.gen._out._iobservable import IObservablefloat
class Observablefloat(Conditional_Impl, IObservablefloat):
    pass


Observable[float] = Observablefloat


from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable import IObservableIOrder
class ObservableIOrder(Conditional_Impl, IObservableIOrder):
    pass


Observable[IOrder] = ObservableIOrder


from marketsim.gen._out._iobservable import IObservablebool
class Observablebool(Conditional_Impl, IObservablebool):
    pass


Observable[bool] = Observablebool


from marketsim.gen._out._icandlestick import ICandleStick
from marketsim.gen._out._iobservable import IObservableICandleStick
class ObservableICandleStick(Conditional_Impl, IObservableICandleStick):
    pass


Observable[ICandleStick] = ObservableICandleStick


from marketsim.gen._out._ivolumelevels import IVolumeLevels
from marketsim.gen._out._iobservable import IObservableIVolumeLevels
class ObservableIVolumeLevels(Conditional_Impl, IObservableIVolumeLevels):
    pass


Observable[IVolumeLevels] = ObservableIVolumeLevels


from marketsim.gen._out._iobservable import IObservableobject
Observable[int]._types.append(IObservablefloat)
Observable[int]._types.append(IObservableobject)
Observable[float]._types.append(IObservableobject)
