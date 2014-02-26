from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._imultiassetstrategy import IMultiAssetStrategy
from marketsim.gen._out._itrader import ITrader
from marketsim import meta
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim import listOf
#(List[.ISingleAssetTrader],.IMultiAssetStrategy,.String,.Float,List[.ITimeSerie]) => .ITrader
class IFunctionITraderlistOfISingleAssetTraderIMultiAssetStrategystrfloatlistOfITimeSerie(object):
    _types = [meta.function((listOf(ISingleAssetTrader),IMultiAssetStrategy,str,float,listOf(ITimeSerie),),ITrader)]
    
    pass



