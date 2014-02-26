from marketsim.gen._out._test.types._r import R
from marketsim.gen._out._ifunction._ifunctiont import IFunctionT
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim import meta
#() => ._test.types.R
class IFunctionR(object):
    _types = [meta.function((),R)]
    _types.append(IFunctionT)
    _types.append(IFunctionobject)
    pass



