from marketsim.gen._out._ifunction._ifunctionbool import IFunctionbool
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._ifunction._ifunctioniobservablefloatiobservablebooliobservablefloatiobservablefloat import IFunctionIObservablefloatIObservableboolIObservablefloatIObservablefloat
from marketsim import meta
#((() => .Boolean),.IObservable[.Float],.IObservable[.Float]) => .IObservable[.Float]
class IFunctionIObservablefloatIFunctionboolIObservablefloatIObservablefloat(object):
    _types = [meta.function((IFunctionbool,IObservablefloat,IObservablefloat,),IObservablefloat)]
    _types.append(IFunctionIObservablefloatIObservableboolIObservablefloatIObservablefloat)
    pass



