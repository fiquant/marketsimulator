from marketsim import listOf
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._ifunction._ifunctionobject_from_listoffloat import IFunctionobject_from_listOffloat
from marketsim import meta
#List[.Float] => (() => Any)
class IFunctionIFunctionobject_from_listOffloat(object):
    _types = [meta.function((listOf(float),),IFunctionobject)]
    _types.append(IFunctionobject_from_listOffloat)
    pass



