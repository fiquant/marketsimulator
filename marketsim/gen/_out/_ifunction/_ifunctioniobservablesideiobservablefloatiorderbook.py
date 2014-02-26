from marketsim.gen._out._side import Side
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import meta
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
class IFunctionIObservableSideIObservablefloatIOrderBook(object):
    _types = [meta.function((IObservablefloat,IOrderBook,),IObservableSide)]
    pass



