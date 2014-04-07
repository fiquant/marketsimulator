from marketsim.gen._out._ifunction._ifunctionifunctionobject_from_iaccount import IFunctionIFunctionobject_from_IAccount
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iaccount import IAccount
from marketsim import meta
from marketsim.gen._out._ifunction._ifunctionobject_from_iaccount import IFunctionobject_from_IAccount
#.IAccount => (() => .Float)
class IFunctionIFunctionfloat_from_IAccount(object):
    _types = [meta.function((IAccount,),IFunctionfloat)]
    _types.append(IFunctionobject_from_IAccount)
    _types.append(IFunctionIFunctionobject_from_IAccount)
    pass



