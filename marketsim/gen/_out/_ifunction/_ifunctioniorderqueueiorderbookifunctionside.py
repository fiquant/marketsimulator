from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim import meta
class IFunctionIOrderQueueIOrderBookIFunctionSide(object):
    _types = [meta.function((IOrderBook,IFunctionSide,),IOrderQueue)]
    pass



