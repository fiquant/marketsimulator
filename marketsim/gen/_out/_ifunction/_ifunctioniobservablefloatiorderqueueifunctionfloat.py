from marketsim.gen._out._ifunction._ifunctioniobservablefloatiorderqueueiobservablefloat import IFunctionIObservablefloatIOrderQueueIObservablefloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim import meta
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
#(.IOrderQueue,(() => .Float)) => .IObservable[.Float]
class IFunctionIObservablefloatIOrderQueueIFunctionfloat(object):
    _types = [meta.function((IOrderQueue,IFunctionfloat,),IObservablefloat)]
    _types.append(IFunctionIObservablefloatIOrderQueueIObservablefloat)
    pass



