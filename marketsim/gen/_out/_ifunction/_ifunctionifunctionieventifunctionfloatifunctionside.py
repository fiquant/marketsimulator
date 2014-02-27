from marketsim.gen._out._ifunction._ifunctionobjectifunctionside import IFunctionobjectIFunctionSide
from marketsim.gen._out._ifunction._ifunctionifunctionobjectifunctionfloatifunctionside import IFunctionIFunctionobjectIFunctionfloatIFunctionSide
from marketsim.gen._out._ifunction._ifunctionieventifunctionfloat import IFunctionIEventIFunctionfloat
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
#(() => .Side) => ((() => .Float) => .IEvent)
class IFunctionIFunctionIEventIFunctionfloatIFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionIEventIFunctionfloat)]
    _types.append(IFunctionobjectIFunctionSide)
    _types.append(IFunctionIFunctionobjectIFunctionfloatIFunctionSide)
    pass



