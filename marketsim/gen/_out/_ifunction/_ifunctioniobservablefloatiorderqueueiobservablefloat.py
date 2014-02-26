from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import meta
#(.IOrderQueue,.IObservable[.Float]) => .IObservable[.Float]
class IFunctionIObservablefloatIOrderQueueIObservablefloat(object):
    _types = [meta.function((IOrderQueue,IObservablefloat,),IObservablefloat)]
    
    pass



