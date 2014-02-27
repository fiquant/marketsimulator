from marketsim.gen._out._ifunction._ifunctionobject_from_listoffloat import IFunctionobject_from_listOffloat
from marketsim.gen._out._ifunction._ifunctionifunctionlistofobject_from_listoffloat import IFunctionIFunctionlistOfobject_from_listOffloat
from marketsim.gen._out._ifunction._ifunctionifunctionobject_from_listoffloat import IFunctionIFunctionobject_from_listOffloat
from marketsim import meta
from marketsim import listOf
from marketsim.gen._out._ifunction._ifunctionlistoffloat import IFunctionlistOffloat
#List[.Float] => (() => List[.Float])
class IFunctionIFunctionlistOffloat_from_listOffloat(object):
    _types = [meta.function((listOf(float),),IFunctionlistOffloat)]
    _types.append(IFunctionobject_from_listOffloat)
    _types.append(IFunctionIFunctionobject_from_listOffloat)
    _types.append(IFunctionIFunctionlistOfobject_from_listOffloat)
    pass



