from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim import meta
#() => (() => .Float)
class IFunctionIFunctionfloat(object):
    _types = [meta.function((),IFunctionfloat)]
    _types.append(IFunctionobject)
    pass



