from marketsim.gen._out._ifunction._ifunctiont import IFunctionT
from marketsim.gen._out._ifunction._ifunctionr import IFunctionR
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._test.types._u import U
from marketsim import meta
#() => ._test.types.U
class IFunctionU(object):
    _types = [meta.function((),U)]
    _types.append(IFunctionobject)
    _types.append(IFunctionT)
    _types.append(IFunctionR)
    pass



