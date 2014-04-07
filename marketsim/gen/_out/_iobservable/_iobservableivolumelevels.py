from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionivolumelevels import IFunctionIVolumeLevels
from marketsim.gen._out._iobservable._iobservableobject import IObservableobject
class IObservableIVolumeLevels(IEvent, IFunctionIVolumeLevels):
    _types = []
    _types.append(IObservableobject)
    pass
