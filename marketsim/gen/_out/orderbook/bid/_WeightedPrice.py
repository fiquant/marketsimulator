from marketsim import IOrderBook
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["Asset", "WeightedPrice"])
class WeightedPrice_IOrderBookFloat(Function[float]):
    """ 
    """ 
    def __init__(self, book = None, alpha = None):
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader
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
        return "[Bid^{%(book)s}]_{%(alpha)s}" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.orderbook._weightedprice import WeightedPrice_IOrderQueueFloat as _orderbook_WeightedPrice
        from marketsim.gen._out.orderbook._bids import Bids_IOrderBook as _orderbook_Bids
        return _orderbook_WeightedPrice(_orderbook_Bids(self.book),self.alpha)
    
def WeightedPrice(book = None,alpha = None): 
    from marketsim import IOrderBook
    from marketsim import float
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return WeightedPrice_IOrderBookFloat(book,alpha)
    raise Exception('Cannot find suitable overload for WeightedPrice('+str(book)+','+str(alpha)+')')
