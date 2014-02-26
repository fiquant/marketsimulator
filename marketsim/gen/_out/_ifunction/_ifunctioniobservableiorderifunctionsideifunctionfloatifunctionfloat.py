from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorder import IOrder
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
#((() => .Side),(() => .Float),(() => .Float)) => .IObservable[.IOrder]
class IFunctionIObservableIOrderIFunctionSideIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionSide,IFunctionfloat,IFunctionfloat,),IObservableIOrder)]
    
    pass



