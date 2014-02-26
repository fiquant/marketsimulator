from marketsim.gen._out._iobservable._iobservableint import IObservableint
from marketsim.gen._out._ifunction._ifunctioniobservablefloatiaccount import IFunctionIObservablefloatIAccount
from marketsim.gen._out._iaccount import IAccount
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionifunctionfloatiaccount import IFunctionIFunctionfloatIAccount
#.IAccount => .IObservable[.Int]
class IFunctionIObservableintIAccount(object):
    _types = [meta.function((IAccount,),IObservableint)]
    _types.append(IFunctionIFunctionfloatIAccount)
    _types.append(IFunctionIObservablefloatIAccount)
    pass



