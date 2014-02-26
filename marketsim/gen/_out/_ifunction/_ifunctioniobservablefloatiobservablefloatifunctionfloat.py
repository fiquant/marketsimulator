from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctioniobservablefloatiobservablefloatiobservablefloat import IFunctionIObservablefloatIObservablefloatIObservablefloat
from marketsim import meta
#(.IObservable[.Float],(() => .Float)) => .IObservable[.Float]
class IFunctionIObservablefloatIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionfloat,),IObservablefloat)]
    _types.append(IFunctionIObservablefloatIObservablefloatIObservablefloat)
    pass



