from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiorderbook import IFunctionIFunctionfloatIOrderBook
from marketsim import meta
#.IOrderBook => .IObservable[.Float]
class IFunctionIObservablefloatIOrderBook(object):
    _types = [meta.function((IOrderBook,),IObservablefloat)]
    _types.append(IFunctionIFunctionfloatIOrderBook)
    pass



