from marketsim import listOf
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim import meta
#() => List[Any]
class IFunctionlistOfobject(object):
    _types = [meta.function((),listOf(object))]
    _types.append(IFunctionobject)
    pass



