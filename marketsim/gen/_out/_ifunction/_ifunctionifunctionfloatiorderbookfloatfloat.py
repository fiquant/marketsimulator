from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim import meta
#(.IOrderBook,.Float,.Float) => (() => .Float)
class IFunctionIFunctionfloatIOrderBookfloatfloat(object):
    _types = [meta.function((IOrderBook,float,float,),IFunctionfloat)]
    
    pass



