from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionifunctionobject_from_ifunctionside import IFunctionIFunctionobject_from_IFunctionSide
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionside import IFunctionobject_from_IFunctionSide
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctioniorder import IFunctionIOrder
#(() => .Side) => (() => .IOrder)
class IFunctionIFunctionIOrder_from_IFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIOrder)]
    _types.append(IFunctionobject_from_IFunctionSide)
    _types.append(IFunctionIFunctionobject_from_IFunctionSide)
    pass



