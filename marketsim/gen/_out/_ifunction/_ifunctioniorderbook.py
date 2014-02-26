from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._ifunction._ifunctionobject import IFunctionobject
from marketsim import meta
#() => .IOrderBook
class IFunctionIOrderBook(object):
    _types = [meta.function((),IOrderBook)]
    _types.append(IFunctionobject)
    pass



