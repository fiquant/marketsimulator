from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import meta
class IFunctionIObservablefloatIOrderBookIFunctionfloat(object):
    _types = [meta.function((IOrderBook,IFunctionfloat,),IObservablefloat)]
    pass



