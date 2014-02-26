from marketsim.gen._out._ifunction._ifunctioniaccountisingleassetstrategy import IFunctionIAccountISingleAssetStrategy
from marketsim import meta
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._ifunction._ifunctionifunctionfloatifunctionfloat import IFunctionIFunctionfloatIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionlistoffloatlistoffloat import IFunctionIFunctionlistOffloatlistOffloat
from marketsim import listOf
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiaccount import IFunctionIFunctionfloatIAccount
#(List[.ISingleAssetStrategy],(.ISingleAssetStrategy => .IAccount),(.IAccount => (() => .Float)),((() => .Float) => (() => .Float)),(List[.Float] => (() => List[.Float]))) => .ISingleAssetStrategy
class IFunctionISingleAssetStrategylistOfISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccountIFunctionIFunctionfloatIFunctionfloatIFunctionIFunctionlistOffloatlistOffloat(object):
    _types = [meta.function((listOf(ISingleAssetStrategy),IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,IFunctionIFunctionfloatIFunctionfloat,IFunctionIFunctionlistOffloatlistOffloat,),ISingleAssetStrategy)]
    
    pass



