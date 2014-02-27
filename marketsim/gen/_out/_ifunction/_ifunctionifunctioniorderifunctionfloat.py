from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionobjectifunctionfloat import IFunctionIFunctionobjectIFunctionfloat
from marketsim.gen._out._ifunction._ifunctioniorder import IFunctionIOrder
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionobjectifunctionfloat import IFunctionobjectIFunctionfloat
#(() => .Float) => (() => .IOrder)
class IFunctionIFunctionIOrderIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIOrder)]
    _types.append(IFunctionobjectIFunctionfloat)
    _types.append(IFunctionIFunctionobjectIFunctionfloat)
    pass



