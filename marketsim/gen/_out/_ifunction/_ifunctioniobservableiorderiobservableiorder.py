from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim import meta
#.IObservable[.IOrder] => .IObservable[.IOrder]
class IFunctionIObservableIOrderIObservableIOrder(object):
    _types = [meta.function((IObservableIOrder,),IObservableIOrder)]
    
    pass


