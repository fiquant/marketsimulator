from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._ievent import IEvent
from marketsim import meta
#(() => .Float) => .IEvent
class IFunctionIEventIFunctionfloat(object):
    _types = [meta.function((IFunctionfloat,),IEvent)]
    
    pass



