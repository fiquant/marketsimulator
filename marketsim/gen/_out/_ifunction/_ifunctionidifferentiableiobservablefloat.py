from marketsim.gen._out._iobservable import IObservablefloat
from marketsim.gen._out._idifferentiable import IDifferentiable
from marketsim import meta
class IFunctionIDifferentiableIObservablefloat(object):
    _types = [meta.function((IObservablefloat,),IDifferentiable)]
    pass



