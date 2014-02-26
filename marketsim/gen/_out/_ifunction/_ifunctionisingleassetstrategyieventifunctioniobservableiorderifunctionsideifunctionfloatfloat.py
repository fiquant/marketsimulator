from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionisingleassetstrategyieventifunctioniobservableiorderifunctionsideiobservablefloatfloat import IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloatfloat
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
from marketsim import meta
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
#(.IEvent,((() => .Side) => .IObservable[.IOrder]),(() => .Float),.Float) => .ISingleAssetStrategy
class IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIFunctionfloatfloat(object):
    _types = [meta.function((IEvent,IFunctionIObservableIOrderIFunctionSide,IFunctionfloat,float,),ISingleAssetStrategy)]
    _types.append(IFunctionISingleAssetStrategyIEventIFunctionIObservableIOrderIFunctionSideIObservablefloatfloat)
    pass



