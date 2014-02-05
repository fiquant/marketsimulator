from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim import IOrderBook
from marketsim import float
from marketsim import context
@registry.expose(["Asset", "WeightedPrice"])
class WeightedPrice_Optional__IOrderBook___Optional__Float_(Function[float]):
    """ 
    """ 
    def __init__(self, book = None, alpha = None):
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim import rtti
        self.book = book if book is not None else _orderbook_OfTrader()
        self.alpha = alpha if alpha is not None else 0.15
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'alpha' : float
    }
    def __repr__(self):
        return "[Ask_{%(book)s}]_{%(alpha)s}" % self.__dict__
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.orderbook._WeightedPrice import WeightedPrice as _orderbook_WeightedPrice
        from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
        return _orderbook_WeightedPrice(_orderbook_Asks(self.book),self.alpha)
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
WeightedPrice = WeightedPrice_Optional__IOrderBook___Optional__Float_
