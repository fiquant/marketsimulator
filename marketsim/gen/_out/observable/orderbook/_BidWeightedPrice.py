from marketsim import registry
from marketsim.ops._function import Function
from marketsim import IOrderBook
from marketsim.gen._out.observable.orderbook._WeightedPrice import WeightedPrice as _observable_orderbook_WeightedPrice
from marketsim.gen._out.observable.orderbook._Bids import Bids as _observable_orderbook_Bids
from marketsim import context
@registry.expose(["Asset's", "BidWeightedPrice"])
class BidWeightedPrice(Function[float]):
    """ 
    """ 
    def __init__(self, book = None, alpha = None):
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader as _observable_orderbook_OfTrader
        self.book = book if book is not None else _observable_orderbook_OfTrader()
        self.alpha = alpha if alpha is not None else 0.015
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'alpha' : float
    }
    def __repr__(self):
        return "Bid_{%(alpha)s}^{%(book)s}" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _observable_orderbook_WeightedPrice(_observable_orderbook_Bids(self.book),self.alpha)
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
