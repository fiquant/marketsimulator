from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim.gen._out._ifunction._ifunctionobject_from_iaccount import IFunctionobject_from_IAccount
from marketsim import meta
#.IAccount => (() => Any)
class IFunctionIFunctionobject_from_IAccount(object):
    _types = [meta.function((IAccount,),IFunctionobject)]
    _types.append(IFunctionobject_from_IAccount)
    pass



