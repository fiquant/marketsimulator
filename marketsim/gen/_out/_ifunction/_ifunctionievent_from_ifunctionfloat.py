from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionfloat import IFunctionobject_from_IFunctionfloat
from marketsim import meta
#(() => .Float) => .IEvent
class IFunctionIEvent_from_IFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IEvent)]
    _types.append(IFunctionobject_from_IFunctionfloat)
    pass



