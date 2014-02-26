from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._ifunction._ifunctioniobservablefloatiobservablefloatiobservablefloat import IFunctionIObservablefloatIObservablefloatIObservablefloat
from marketsim import meta
#((() => .Float),.IObservable[.Float]) => .IObservable[.Float]
class IFunctionIObservablefloatIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionfloat,IObservablefloat,),IObservablefloat)]
    _types.append(IFunctionIObservablefloatIObservablefloatIObservablefloat)
    pass



