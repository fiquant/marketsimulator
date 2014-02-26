from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iaccount import IAccount
from marketsim import meta
#.ISingleAssetStrategy => .IAccount
class IFunctionIAccountISingleAssetStrategy(object):
    _types = [meta.function((ISingleAssetStrategy,),IAccount)]
    
    pass



