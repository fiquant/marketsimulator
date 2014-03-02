from marketsim import registry
from marketsim.gen._out._iorderbook import IOrderBook
@registry.expose(["-", "MeanReversion"])
class MeanReversion_FloatIOrderBook(object):
    """ 
    """ 
    def __init__(self, alpha = None, book = None):
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import deref_opt
        from marketsim import rtti
        self.alpha = alpha if alpha is not None else 0.015
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "MeanReversion(%(alpha)s, %(book)s)" % self.__dict__
    

    @property
    def Book(self):
        from marketsim.gen._out.strategy.side._book import Book
        return Book(self)
    
    @property
    def Alpha(self):
        from marketsim.gen._out.strategy.side._alpha import Alpha
        return Alpha(self)
    
    def Strategy(self, eventGen = None,orderFactory = None):
        from marketsim.gen._out.strategy.side._strategy import Strategy
        return Strategy(self,eventGen,orderFactory)
    
    @property
    def Side(self):
        from marketsim.gen._out.strategy.side._side import Side
        return Side(self)
    
    pass
MeanReversion = MeanReversion_FloatIOrderBook
