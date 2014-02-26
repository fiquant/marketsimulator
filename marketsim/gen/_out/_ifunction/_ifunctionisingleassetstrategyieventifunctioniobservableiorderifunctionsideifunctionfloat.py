from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
from marketsim.gen._out._ifunction._ifunctionisingleassetstrategyieventifunctioniobservableiorderifunctionsideiobservablefloat import IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloat
from marketsim import meta
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
#(.IEvent,((() => .Side) => .IObservable[.IOrder]),(() => .Float)) => .ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,),ISingleAssetStrategy)]
    _types.append(IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloat)
    pass



