from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim import meta
#(.IOrderBook,.Float,.IOrderBook) => .IObservable[.Side]
class IFunctionIObservableSideIOrderBookfloatIOrderBook(object):
    _types = [meta.function((IOrderBook,float,IOrderBook,),IObservableSide)]
    
    pass



