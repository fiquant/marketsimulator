from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import meta
class IFunctionIObservablefloatIOrderQueueIFunctionfloat(object):
    _types = [meta.function((IOrderQueue,IFunctionfloat,),IObservablefloat)]
    pass



