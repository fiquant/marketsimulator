from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import meta
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim import listOf
#(.IOrderBook,.ISingleAssetStrategy,.String,.Float,.Float,List[.ITimeSerie]) => .ISingleAssetTrader
class IFunctionISingleAssetTraderIOrderBookISingleAssetStrategystrfloatfloatlistOfITimeSerie(object):
    _types = [meta.function((IOrderBook,ISingleAssetStrategy,str,float,float,listOf(ITimeSerie),),ISingleAssetTrader)]
    
    pass



