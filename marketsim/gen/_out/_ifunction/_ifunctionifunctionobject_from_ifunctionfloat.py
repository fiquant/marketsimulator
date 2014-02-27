from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._ifunction._ifunctionobject_from_ifunctionfloat import IFunctionobject_from_IFunctionfloat
from marketsim import meta
#(() => .Float) => (() => Any)
class IFunctionIFunctionobject_from_IFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionobject)]
    _types.append(IFunctionobject_from_IFunctionfloat)
    pass



