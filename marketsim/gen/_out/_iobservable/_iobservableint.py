from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionint import IFunctionint
from marketsim.gen._out._iobservable._iobservableobject import IObservableobject
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
class IObservableint(IEvent, IFunctionint):
    _types = []
    _types.append(IObservableobject)
    _types.append(IObservablefloat)
    pass
