from marketsim.gen._out._iaccount import IAccount
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import meta
#(.IAccount,.Float) => (() => .Float)
class IFunctionIFunctionfloatIAccountfloat(object):
    _types = [meta.function((IAccount,float,),IFunctionfloat)]
    
    pass



