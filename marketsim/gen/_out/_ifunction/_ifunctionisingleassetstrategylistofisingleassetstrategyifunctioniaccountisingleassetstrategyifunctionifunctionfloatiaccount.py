from marketsim.gen._out._ifunction._ifunctioniaccountisingleassetstrategy import IFunctionIAccountISingleAssetStrategy
from marketsim import meta
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import listOf
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiaccount import IFunctionIFunctionfloatIAccount
#(List[.ISingleAssetStrategy],(.ISingleAssetStrategy => .IAccount),(.IAccount => (() => .Float))) => .ISingleAssetStrategy
class IFunctionISingleAssetStrategylistOfISingleAssetStrategyIFunctionIAccountISingleAssetStrategyIFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((listOf(ISingleAssetStrategy),IFunctionIAccountISingleAssetStrategy,IFunctionIFunctionfloatIAccount,),ISingleAssetStrategy)]
    
    pass



