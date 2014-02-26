from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim import meta
class IFunctionIOrderQueueIOrderBook(object):
    _types = [meta.function((IOrderBook,),IOrderQueue)]
    pass



