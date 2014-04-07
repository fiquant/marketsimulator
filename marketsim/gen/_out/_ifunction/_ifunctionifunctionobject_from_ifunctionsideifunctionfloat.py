from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionsideifunctionfloat import IFunctionobject_from_IFunctionSideIFunctionfloat
from marketsim import meta
#((() => .Side),(() => .Float)) => (() => Any)
class IFunctionIFunctionobject_from_IFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionobject)]
    _types.append(IFunctionobject_from_IFunctionSideIFunctionfloat)
    pass



