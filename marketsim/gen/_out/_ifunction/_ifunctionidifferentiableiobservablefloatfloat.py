from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiobservablefloatfloat import IFunctionIFunctionfloatIObservablefloatfloat
from marketsim import meta
#(.IObservable[.Float],.Float) => .IDifferentiable
class IFunctionIDifferentiableIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IDifferentiable)]
    _types.append(IFunctionIFunctionfloatIObservablefloatfloat)
    pass



