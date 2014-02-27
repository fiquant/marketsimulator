from marketsim.gen._out._ifunction._ifunctionobjectiaccount import IFunctionobjectIAccount
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ifunction._ifunctionifunctionobjectiaccount import IFunctionIFunctionobjectIAccount
from marketsim.gen._out._iaccount import IAccount
from marketsim import meta
#.IAccount => (() => .Float)
class IFunctionIFunctionfloatIAccount(object):
    _types = [meta.function((IAccount,),IFunctionfloat)]
    _types.append(IFunctionobjectIAccount)
    _types.append(IFunctionIFunctionobjectIAccount)
    pass



