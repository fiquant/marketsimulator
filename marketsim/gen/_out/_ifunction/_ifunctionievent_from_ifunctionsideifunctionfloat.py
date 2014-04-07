from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionsideifunctionfloat import IFunctionobject_from_IFunctionSideIFunctionfloat
from marketsim import meta
#((() => .Side),(() => .Float)) => .IEvent
class IFunctionIEvent_from_IFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IEvent)]
    _types.append(IFunctionobject_from_IFunctionSideIFunctionfloat)
    pass



