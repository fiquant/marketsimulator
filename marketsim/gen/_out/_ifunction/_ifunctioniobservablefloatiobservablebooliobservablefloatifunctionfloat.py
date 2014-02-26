from marketsim.gen._out._ifunction._ifunctioniobservablefloatiobservablebooliobservablefloatiobservablefloat import IFunctionIObservablefloatIObservableboolIObservablefloatIObservablefloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import meta
from marketsim.gen._out._iobservable._iobservablebool import IObservablebool
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
#(.IObservable[.Boolean],.IObservable[.Float],(() => .Float)) => .IObservable[.Float]
class IFunctionIObservablefloatIObservableboolIObservablefloatIFunctionfloat(object):
    _types = [meta.function((IObservablebool,IObservablefloat,IFunctionfloat,),IObservablefloat)]
    _types.append(IFunctionIObservablefloatIObservableboolIObservablefloatIObservablefloat)
    pass



