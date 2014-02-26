from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._ifunction._ifunctionifunctionfloatfloat import IFunctionIFunctionfloatfloat
from marketsim import meta
#.Float => .IObservable[.Float]
class IFunctionIObservablefloatfloat(object):
    _types = [meta.function((float,),IObservablefloat)]
    _types.append(IFunctionIFunctionfloatfloat)
    pass



