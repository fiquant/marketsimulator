from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctioniobservablefloatiorderbookiobservablefloat import IFunctionIObservablefloatIOrderBookIObservablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
#(.IOrderBook,(() => .Float)) => .IObservable[.Float]
class IFunctionIObservablefloatIOrderBookIFunctionfloat(object):
    _types = [meta.function((IOrderBook,IFunctionfloat,),IObservablefloat)]
    _types.append(IFunctionIObservablefloatIOrderBookIObservablefloat)
    pass



