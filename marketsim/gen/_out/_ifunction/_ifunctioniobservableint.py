from marketsim.gen._out._ifunction._ifunctionifunctionfloat import IFunctionIFunctionfloat
from marketsim.gen._out._iobservable._iobservableint import IObservableint
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._ifunction._ifunctionifunctionint import IFunctionIFunctionint
from marketsim import meta
#() => .IObservable[.Int]
class IFunctionIObservableint(object):
    _types = [meta.function((),IObservableint)]
    _types.append(IFunctionobject)
    _types.append(IFunctionIFunctionint)
    _types.append(IFunctionIFunctionfloat)
    pass



