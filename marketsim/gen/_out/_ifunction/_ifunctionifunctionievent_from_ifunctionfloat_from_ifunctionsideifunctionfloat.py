from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionievent_from_ifunctionfloat import IFunctionIEvent_from_IFunctionfloat
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionifunctionobject_from_ifunctionfloat_from_ifunctionsideifunctionfloat import IFunctionIFunctionobject_from_IFunctionfloat_from_IFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionsideifunctionfloat import IFunctionobject_from_IFunctionSideIFunctionfloat
#((() => .Side),(() => .Float)) => ((() => .Float) => .IEvent)
class IFunctionIFunctionIEvent_from_IFunctionfloat_from_IFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,),IFunctionIEvent_from_IFunctionfloat)]
    _types.append(IFunctionobject_from_IFunctionSideIFunctionfloat)
    _types.append(IFunctionIFunctionobject_from_IFunctionfloat_from_IFunctionSideIFunctionfloat)
    pass



