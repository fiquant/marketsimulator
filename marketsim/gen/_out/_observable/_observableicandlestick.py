from marketsim.gen._out._icandlestick import ICandleStick
from marketsim.gen._out._iobservable._iobservableicandlestick import IObservableICandleStick
from marketsim.gen._out._observable._observableobject import Observableobject
from marketsim.event import Conditional_Impl
class ObservableICandleStick(Conditional_Impl, IObservableICandleStick):
    _types = []
    _types.append(Observableobject)



