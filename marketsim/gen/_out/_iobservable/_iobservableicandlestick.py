from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionicandlestick import IFunctionICandleStick
from marketsim.gen._out._iobservable._iobservableobject import IObservableobject
class IObservableICandleStick(IEvent, IFunctionICandleStick):
    _types = []
    _types.append(IObservableobject)
    pass
