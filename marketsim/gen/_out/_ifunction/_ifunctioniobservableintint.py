from marketsim.gen._out._iobservable._iobservableint import IObservableint
from marketsim.gen._out._ifunction._ifunctionifunctionintint import IFunctionIFunctionintint
from marketsim import meta
#.Int => .IObservable[.Int]
class IFunctionIObservableintint(object):
    _types = [meta.function((int,),IObservableint)]
    _types.append(IFunctionIFunctionintint)
    pass



