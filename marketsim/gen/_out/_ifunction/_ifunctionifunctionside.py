from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim import meta
#() => (() => .Side)
class IFunctionIFunctionSide(object):
    _types = [meta.function((),IFunctionSide)]
    _types.append(IFunctionobject)
    pass



