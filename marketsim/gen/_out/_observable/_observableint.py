from marketsim.gen._out._iobservable._iobservableint import IObservableint
from marketsim.gen._out._observable._observableobject import Observableobject
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.event import Conditional_Impl
class Observableint(Conditional_Impl, IObservableint):
    _types = []
    _types.append(Observableobject)
    _types.append(Observablefloat)



