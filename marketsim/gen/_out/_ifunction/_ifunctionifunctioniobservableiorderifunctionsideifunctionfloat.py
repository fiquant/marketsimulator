from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
from marketsim import meta
#(() => .Float) => ((() => .Side) => .IObservable[.IOrder])
class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionIObservableIOrderIFunctionSide)]
    
    pass



from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionsideifunctionfloat import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim import meta
#() => (((() => .Side),(() => .Float)) => .IObservable[.IOrder])
class IFunctionIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((),IFunctionIObservableIOrderIFunctionSideIFunctionfloat)]
    _types.append(IFunctionobject)
    pass



