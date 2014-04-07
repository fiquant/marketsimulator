from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._observable._observableobject import Observableobject
from marketsim.event import Conditional_Impl
class Observablefloat(Conditional_Impl, IObservablefloat):
    _types = []
    _types.append(Observableobject)



