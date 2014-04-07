from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._ifunction._ifunctionobject_from_isingleassetstrategy import IFunctionobject_from_ISingleAssetStrategy
from marketsim import meta
#.ISingleAssetStrategy => .IAccount
class IFunctionIAccount_from_ISingleAssetStrategy(object):
    _types = [meta.function((ISingleAssetStrategy,),IAccount)]
    _types.append(IFunctionobject_from_ISingleAssetStrategy)
    pass



