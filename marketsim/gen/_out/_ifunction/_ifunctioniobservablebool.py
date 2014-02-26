from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._ifunction._ifunctionifunctionbool import IFunctionIFunctionbool
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim import meta
#() => .IObservable[.Boolean]
class IFunctionIObservablebool(object):
    _types = [meta.function((),IObservablebool)]
    _types.append(IFunctionIFunctionbool)
    _types.append(IFunctionobject)
    pass



