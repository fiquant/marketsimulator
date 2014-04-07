from marketsim.gen._out._ivolumelevels import IVolumeLevels
from marketsim.gen._out._iobservable._iobservableivolumelevels import IObservableIVolumeLevels
from marketsim.gen._out._observable._observableobject import Observableobject
from marketsim.event import Conditional_Impl
class ObservableIVolumeLevels(Conditional_Impl, IObservableIVolumeLevels):
    _types = []
    _types.append(Observableobject)



