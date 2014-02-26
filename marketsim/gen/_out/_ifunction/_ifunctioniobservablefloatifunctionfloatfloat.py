from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionfloatifunctionfloatfloat import IFunctionIFunctionfloatIFunctionfloatfloat
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctioniobservablefloatiobservablefloatfloat import IFunctionIObservablefloatIObservablefloatfloat
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiobservablefloatfloat import IFunctionIFunctionfloatIObservablefloatfloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
#((() => .Float),.Float) => .IObservable[.Float]
class IFunctionIObservablefloatIFunctionfloatfloat(object):
    _types = [meta.function((IFunctionfloat,float,),IObservablefloat)]
    _types.append(IFunctionIFunctionfloatIFunctionfloatfloat)
    _types.append(IFunctionIFunctionfloatIObservablefloatfloat)
    _types.append(IFunctionIObservablefloatIObservablefloatfloat)
    pass



