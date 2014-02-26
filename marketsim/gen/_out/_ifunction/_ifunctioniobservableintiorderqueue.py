from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim.gen._out._iobservable._iobservableint import IObservableint
from marketsim.gen._out._ifunction._ifunctioniobservablefloatiorderqueue import IFunctionIObservablefloatIOrderQueue
from marketsim import meta
#.IOrderQueue => .IObservable[.Int]
class IFunctionIObservableintIOrderQueue(object):
    _types = [meta.function((IOrderQueue,),IObservableint)]
    _types.append(IFunctionIObservablefloatIOrderQueue)
    pass



