from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim import listOf
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import meta
class IFunctionIOrderBookstrfloatintlistOfITimeSerie(object):
    _types = [meta.function((str,float,int,listOf(ITimeSerie),),IOrderBook)]
    pass



