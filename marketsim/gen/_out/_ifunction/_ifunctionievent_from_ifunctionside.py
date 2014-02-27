from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionside import IFunctionobject_from_IFunctionSide
from marketsim import meta
#(() => .Side) => .IEvent
class IFunctionIEvent_from_IFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IEvent)]
    _types.append(IFunctionobject_from_IFunctionSide)
    pass



