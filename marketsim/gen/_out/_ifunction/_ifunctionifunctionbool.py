from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim import meta
#() => (() => .Boolean)
class IFunctionIFunctionbool(object):
    _types = [meta.function((),IFunctionbool)]
    _types.append(IFunctionobject)
    pass



