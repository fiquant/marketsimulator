from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._side import Side
from marketsim import meta
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._ifunction._ifunctionifunctionside import IFunctionIFunctionSide
#() => .IObservable[.Side]
class IFunctionIObservableSide(object):
    _types = [meta.function((),IObservableSide)]
    _types.append(IFunctionobject)
    _types.append(IFunctionIFunctionSide)
    pass



