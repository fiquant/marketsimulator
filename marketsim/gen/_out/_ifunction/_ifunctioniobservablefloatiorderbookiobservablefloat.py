from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import meta
#(.IOrderBook,.IObservable[.Float]) => .IObservable[.Float]
class IFunctionIObservablefloatIOrderBookIObservablefloat(object):
    _types = [meta.function((IOrderBook,IObservablefloat,),IObservablefloat)]
    
    pass



