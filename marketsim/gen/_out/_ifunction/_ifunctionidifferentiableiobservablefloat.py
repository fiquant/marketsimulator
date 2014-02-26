from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiobservablefloat import IFunctionIFunctionfloatIObservablefloat
from marketsim import meta
#.IObservable[.Float] => .IDifferentiable
class IFunctionIDifferentiableIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),IDifferentiable)]
    _types.append(IFunctionIFunctionfloatIObservablefloat)
    pass



