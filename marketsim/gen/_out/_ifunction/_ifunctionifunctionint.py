from marketsim.gen._out._ifunction._ifunctionint import IFunctionint
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._ifunction._ifunctionifunctionfloat import IFunctionIFunctionfloat
from marketsim import meta
#() => (() => .Int)
class IFunctionIFunctionint(object):
    _types = [meta.function((),IFunctionint)]
    _types.append(IFunctionobject)
    _types.append(IFunctionIFunctionfloat)
    pass



