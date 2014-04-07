from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionfloat import IFunctionobject_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionobject_from_ifunctionfloat import IFunctionIFunctionobject_from_IFunctionfloat
from marketsim import meta
#(() => .Float) => (() => .Float)
class IFunctionIFunctionfloat_from_IFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionfloat)]
    _types.append(IFunctionobject_from_IFunctionfloat)
    _types.append(IFunctionIFunctionobject_from_IFunctionfloat)
    pass



