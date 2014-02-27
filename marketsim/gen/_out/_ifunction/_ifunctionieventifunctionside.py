from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionobjectifunctionside import IFunctionobjectIFunctionSide
from marketsim import meta
#(() => .Side) => .IEvent
class IFunctionIEventIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IEvent)]
    _types.append(IFunctionobjectIFunctionSide)
    pass



