from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionsideifunctionfloat import IFunctionobject_from_IFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionobject_from_ifunctionsideifunctionfloat import IFunctionIFunctionobject_from_IFunctionSideIFunctionfloat
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctioniorder import IFunctionIOrder
#((() => .Side),(() => .Float)) => (() => .IOrder)
class IFunctionIFunctionIOrder_from_IFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionIOrder)]
    _types.append(IFunctionobject_from_IFunctionSideIFunctionfloat)
    _types.append(IFunctionIFunctionobject_from_IFunctionSideIFunctionfloat)
    pass



