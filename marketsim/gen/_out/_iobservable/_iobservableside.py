from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservableobject import IObservableobject
class IObservableSide(IEvent, IFunctionSide):
    _types = []
    _types.append(IObservableobject)
    pass
