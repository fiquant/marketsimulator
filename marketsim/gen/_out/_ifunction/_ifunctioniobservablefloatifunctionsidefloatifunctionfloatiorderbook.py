from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
#((() => .Side),.Float,(() => .Float),.IOrderBook) => .IObservable[.Float]
class IFunctionIObservablefloatIFunctionSidefloatIFunctionfloatIOrderBook(object):
    _types = [meta.function((IFunctionSide,float,IFunctionfloat,IOrderBook,),IObservablefloat)]
    
    pass



