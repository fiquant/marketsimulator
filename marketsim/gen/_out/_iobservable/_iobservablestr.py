from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionstr import IFunctionstr
from marketsim.gen._out._iobservable._iobservableobject import IObservableobject
class IObservablestr(IEvent, IFunctionstr):
    _types = []
    _types.append(IObservableobject)
    pass
