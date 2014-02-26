from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiaccount import IFunctionIFunctionfloatIAccount
from marketsim import meta
#.IAccount => .IObservable[.Float]
class IFunctionIObservablefloatIAccount(object):
    _types = [meta.function((IAccount,),IObservablefloat)]
    _types.append(IFunctionIFunctionfloatIAccount)
    pass



