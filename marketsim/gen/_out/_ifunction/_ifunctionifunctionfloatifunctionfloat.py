from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionfloatidifferentiable import IFunctionIFunctionfloatIDifferentiable
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiobservablefloat import IFunctionIFunctionfloatIObservablefloat
from marketsim import meta
#(() => .Float) => (() => .Float)
class IFunctionIFunctionfloatIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IFunctionfloat)]
    _types.append(IFunctionIFunctionfloatIDifferentiable)
    _types.append(IFunctionIFunctionfloatIObservablefloat)
    pass



