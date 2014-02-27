from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionobjectifunctionsideifunctionfloat import IFunctionobjectIFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
#((() => .Side),(() => .Float)) => .IEvent
class IFunctionIEventIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IEvent)]
    _types.append(IFunctionobjectIFunctionSideIFunctionfloat)
    pass



