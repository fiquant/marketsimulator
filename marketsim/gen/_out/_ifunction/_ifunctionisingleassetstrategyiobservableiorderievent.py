from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._iorder import IOrder
from marketsim import meta
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
class IFunctionISingleAssetStrategyIObservableIOrderIEvent(object):
    _types = [meta.function((IObservableIOrder,IEvent,),ISingleAssetStrategy)]
    pass



