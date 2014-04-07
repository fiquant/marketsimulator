from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionfloat import IFunctionobject_from_IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionside import IFunctionobject_from_IFunctionSide
from marketsim import meta
#(() => .Side) => ((() => .Float) => Any)
class IFunctionIFunctionobject_from_IFunctionfloat_from_IFunctionSide(object):
    _types = [meta.function((IFunctionSide,),IFunctionobject_from_IFunctionfloat)]
    _types.append(IFunctionobject_from_IFunctionSide)
    pass



