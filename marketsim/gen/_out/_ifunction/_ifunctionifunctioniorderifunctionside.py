from marketsim.gen._out._ifunction._ifunctionobjectifunctionside import IFunctionobjectIFunctionSide
from marketsim.gen._out._ifunction._ifunctioniorder import IFunctionIOrder
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionifunctionobjectifunctionside import IFunctionIFunctionobjectIFunctionSide
#(() => .Side) => (() => .IOrder)
class IFunctionIFunctionIOrderIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIOrder)]
    _types.append(IFunctionobjectIFunctionSide)
    _types.append(IFunctionIFunctionobjectIFunctionSide)
    pass



