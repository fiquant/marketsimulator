from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._observable._observableobject import Observableobject
from marketsim.event import Conditional_Impl
class Observablebool(Conditional_Impl, IObservablebool):
    _types = []
    _types.append(Observableobject)



