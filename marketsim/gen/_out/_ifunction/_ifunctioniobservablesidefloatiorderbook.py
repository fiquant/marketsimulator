from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable import IObservableSide
from marketsim import meta
class IFunctionIObservableSidefloatIOrderBook(object):
    _types = [meta.function((float,IOrderBook,),IObservableSide)]
    pass



