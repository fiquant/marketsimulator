from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._side import Side
from marketsim.gen._out._iobservable._iobservableside import IObservableSide
from marketsim import meta
#(.IObservable[.Float],.Float) => .IObservable[.Side]
class IFunctionIObservableSideIObservablefloatfloat(object):
    _types = [meta.function((IObservablefloat,float,),IObservableSide)]
    
    pass



