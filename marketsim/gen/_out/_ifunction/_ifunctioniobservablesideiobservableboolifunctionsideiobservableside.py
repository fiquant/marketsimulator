from marketsim.gen._out._side import Side
from marketsim.gen._out._ifunction._ifunctioniobservablesideiobservablebooliobservablesideiobservableside import IFunctionIObservableSideIObservableboolIObservableSideIObservableSide
from marketsim import meta
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
#(.IObservable[.Boolean],(() => .Side),.IObservable[.Side]) => .IObservable[.Side]
class IFunctionIObservableSideIObservableboolIFunctionSideIObservableSide(object):
    _types = [meta.function((IObservablebool,IFunctionSide,IObservableSide,),IObservableSide)]
    _types.append(IFunctionIObservableSideIObservableboolIObservableSideIObservableSide)
    pass



