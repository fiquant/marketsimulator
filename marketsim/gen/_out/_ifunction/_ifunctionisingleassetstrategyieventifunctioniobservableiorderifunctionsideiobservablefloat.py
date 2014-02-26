from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
from marketsim import meta
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
#(.IEvent,((() => .Side) => .IObservable[.IOrder]),.IObservable[.Float]) => .ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IObservablefloat,),ISingleAssetStrategy)]
    
    pass



