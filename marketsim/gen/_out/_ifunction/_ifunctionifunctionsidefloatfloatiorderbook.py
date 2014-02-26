from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim import meta
#(.Float,.Float,.IOrderBook) => (() => .Side)
class IFunctionIFunctionSidefloatfloatIOrderBook(object):
    _types = [meta.function((float,float,IOrderBook,),IFunctionSide)]
    
    pass



