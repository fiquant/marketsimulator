from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionside import IFunctionobject_from_IFunctionSide
from marketsim import meta
#(() => .Side) => (() => Any)
class IFunctionIFunctionobject_from_IFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionobject)]
    _types.append(IFunctionobject_from_IFunctionSide)
    pass



