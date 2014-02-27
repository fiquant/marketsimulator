from marketsim.gen._out._ifunction._ifunctionobject_from_listoffloat import IFunctionobject_from_listOffloat
from marketsim.gen._out._ifunction._ifunctionlistofobject import IFunctionlistOfobject
from marketsim.gen._out._ifunction._ifunctionifunctionobject_from_listoffloat import IFunctionIFunctionobject_from_listOffloat
from marketsim import meta
from marketsim import listOf
#List[.Float] => (() => List[Any])
class IFunctionIFunctionlistOfobject_from_listOffloat(object):
    _types = [meta.function((listOf(float),),IFunctionlistOfobject)]
    _types.append(IFunctionobject_from_listOffloat)
    _types.append(IFunctionIFunctionobject_from_listOffloat)
    pass



