from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiobservablefloatfloatfloatfloatfloat import IFunctionIFunctionfloatIObservablefloatfloatfloatfloatfloat
from marketsim import meta
#(.IObservable[.Float],.Float,.Float,.Float,.Float) => .IDifferentiable
class IFunctionIDifferentiableIObservablefloatfloatfloatfloatfloat(object):
    _types = [meta.function((IObservablefloat,float,float,float,float,),IDifferentiable)]
    _types.append(IFunctionIFunctionfloatIObservablefloatfloatfloatfloatfloat)
    pass



