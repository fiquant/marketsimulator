from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionfloat import IFunctionobject_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionsideifunctionfloat import IFunctionobject_from_IFunctionSideIFunctionfloat
#((() => .Side),(() => .Float)) => ((() => .Float) => Any)
class IFunctionIFunctionobject_from_IFunctionfloat_from_IFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionobject_from_IFunctionfloat)]
    _types.append(IFunctionobject_from_IFunctionSideIFunctionfloat)
    pass



