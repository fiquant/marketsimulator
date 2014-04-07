from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._iobservable._iobservableobject import IObservableobject
class IObservablebool(IEvent, IFunctionbool):
    _types = []
    _types.append(IObservableobject)
    pass
