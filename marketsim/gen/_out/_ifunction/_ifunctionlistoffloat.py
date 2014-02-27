from marketsim import listOf
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._ifunction._ifunctionlistofobject import IFunctionlistOfobject
from marketsim import meta
#() => List[.Float]
class IFunctionlistOffloat(object):
    _types = [meta.function((),listOf(float))]
    _types.append(IFunctionobject)
    _types.append(IFunctionlistOfobject)
    pass



