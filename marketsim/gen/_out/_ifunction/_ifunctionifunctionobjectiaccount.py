from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._ifunction._ifunctionobjectiaccount import IFunctionobjectIAccount
from marketsim import meta
#.IAccount => (() => Any)
class IFunctionIFunctionobjectIAccount(object):
    _types = [meta.function((IAccount,),IFunctionobject)]
    _types.append(IFunctionobjectIAccount)
    pass



