from marketsim.gen._out._ifunction._ifunctionifunctionobjectlistoffloat import IFunctionIFunctionobjectlistOffloat
from marketsim.gen._out._ifunction._ifunctionlistofobject import IFunctionlistOfobject
from marketsim.gen._out._ifunction._ifunctionobjectlistoffloat import IFunctionobjectlistOffloat
from marketsim import meta
from marketsim import listOf
#List[.Float] => (() => List[Any])
class IFunctionIFunctionlistOfobjectlistOffloat(object):
    _types = [meta.function((listOf(float),),IFunctionlistOfobject)]
    _types.append(IFunctionobjectlistOffloat)
    _types.append(IFunctionIFunctionobjectlistOffloat)
    pass



