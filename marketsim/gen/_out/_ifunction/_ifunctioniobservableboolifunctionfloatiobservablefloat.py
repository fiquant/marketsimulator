from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctioniobservablebooliobservablefloatiobservablefloat import IFunctionIObservableboolIObservablefloatIObservablefloat
from marketsim import meta
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
#((() => .Float),.IObservable[.Float]) => .IObservable[.Boolean]
class IFunctionIObservableboolIFunctionfloatIObservablefloat(object):
    _types = [meta.function((IFunctionfloat,IObservablefloat,),IObservablebool)]
    _types.append(IFunctionIObservableboolIObservablefloatIObservablefloat)
    pass



