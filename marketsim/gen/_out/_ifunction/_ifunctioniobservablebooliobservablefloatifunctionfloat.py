from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctioniobservablebooliobservablefloatiobservablefloat import IFunctionIObservableboolIObservablefloatIObservablefloat
from marketsim import meta
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
#(.IObservable[.Float],(() => .Float)) => .IObservable[.Boolean]
class IFunctionIObservableboolIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IObservablefloat,IFunctionfloat,),IObservablebool)]
    _types.append(IFunctionIObservableboolIObservablefloatIObservablefloat)
    pass



