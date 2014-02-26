from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
from marketsim import meta
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
#(.IEvent,((() => .Side) => .IObservable[.IOrder]),.IOrderBook,.Float) => .ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIOrderBookfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IOrderBook,float,),ISingleAssetStrategy)]
    
    pass



