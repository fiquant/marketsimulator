from marketsim import listOf
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._ifunction._ifunctionobjectlistoffloat import IFunctionobjectlistOffloat
from marketsim import meta
#List[.Float] => (() => Any)
class IFunctionIFunctionobjectlistOffloat(object):
    _types = [meta.function((listOf(float),),IFunctionobject)]
    _types.append(IFunctionobjectlistOffloat)
    pass



