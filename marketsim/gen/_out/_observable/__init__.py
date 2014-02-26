from marketsim.event import Conditional_Impl
Observable = {}
from _observableint import Observableint
Observable[int] = Observableint


from marketsim.gen._out._side import Side
from _observableside import ObservableSide
Observable[Side] = ObservableSide


from _observablefloat import Observablefloat
Observable[float] = Observablefloat


from marketsim.gen._out._iorder import IOrder
from _observableiorder import ObservableIOrder
Observable[IOrder] = ObservableIOrder


from _observablebool import Observablebool
Observable[bool] = Observablebool


from marketsim.gen._out._icandlestick import ICandleStick
from _observableicandlestick import ObservableICandleStick
Observable[ICandleStick] = ObservableICandleStick


from marketsim.gen._out._ivolumelevels import IVolumeLevels
from _observableivolumelevels import ObservableIVolumeLevels
Observable[IVolumeLevels] = ObservableIVolumeLevels


from marketsim.gen._out._iobservable._iobservableobject import IObservableobject
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
Observable[int]._types.append(IObservablefloat)
Observable[int]._types.append(IObservableobject)
Observable[float]._types.append(IObservableobject)
