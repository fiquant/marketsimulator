from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionside import IFunctionobject_from_IFunctionSide
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionievent_from_ifunctionfloat import IFunctionIEvent_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionobject_from_ifunctionfloat_from_ifunctionside import IFunctionIFunctionobject_from_IFunctionfloat_from_IFunctionSide
#(() => .Side) => ((() => .Float) => .IEvent)
class IFunctionIFunctionIEvent_from_IFunctionfloat_from_IFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIEvent_from_IFunctionfloat)]
    _types.append(IFunctionobject_from_IFunctionSide)
    _types.append(IFunctionIFunctionobject_from_IFunctionfloat_from_IFunctionSide)
    pass



