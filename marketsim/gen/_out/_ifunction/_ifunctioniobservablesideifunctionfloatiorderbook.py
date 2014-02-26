from marketsim.gen._out._ifunction._ifunctioniobservablesideiobservablefloatiorderbook import IFunctionIObservableSideIObservablefloatIOrderBook
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._side import Side
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import meta
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
#((() => .Float),.IOrderBook) => .IObservable[.Side]
class IFunctionIObservableSideIFunctionfloatIOrderBook(object):
    _types = [meta.function((IFunctionfloat,IOrderBook,),IObservableSide)]
    _types.append(IFunctionIObservableSideIObservablefloatIOrderBook)
    pass



