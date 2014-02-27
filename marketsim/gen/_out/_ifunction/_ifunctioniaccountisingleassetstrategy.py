from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._ifunction._ifunctionobjectisingleassetstrategy import IFunctionobjectISingleAssetStrategy
from marketsim import meta
#.ISingleAssetStrategy => .IAccount
class IFunctionIAccountISingleAssetStrategy(object):
    _types = [meta.function((ISingleAssetStrategy,),IAccount)]
    _types.append(IFunctionobjectISingleAssetStrategy)
    pass



