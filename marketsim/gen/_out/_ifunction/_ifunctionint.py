from marketsim.types import Function_impl
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import meta
#() => .Int
class IFunctionint(Function_impl):
    _types = [meta.function((),int)]
    _types.append(IFunctionobject)
    _types.append(IFunctionfloat)
    pass



