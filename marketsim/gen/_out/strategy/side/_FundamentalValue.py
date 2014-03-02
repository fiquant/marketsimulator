from marketsim import registry
from marketsim.gen._out.strategy.side._sidestrategy import SideStrategy
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorderbook import IOrderBook
@registry.expose(["-", "FundamentalValue"])
class FundamentalValue_FloatIOrderBook(SideStrategy):
    """ 
    """ 
    def __init__(self, fv = None, book = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import rtti
        self.fv = fv if fv is not None else deref_opt(_constant_Float(200.0))
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'fv' : IFunctionfloat,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "FundamentalValue(%(fv)s, %(book)s)" % self.__dict__
    

    @property
    def Side(self):
        from marketsim.gen._out.strategy.side._side import Side
        return Side(self)
    
    def Strategy(self, eventGen = None,orderFactory = None):
        from marketsim.gen._out.strategy.side._strategy import Strategy
        return Strategy(self,eventGen,orderFactory)
    
    @property
    def Book(self):
        from marketsim.gen._out.strategy.side._book import Book
        return Book(self)
    
    @property
    def FV_Side(self):
        from marketsim.gen._out.strategy.side._fv_side import FV_Side
        return FV_Side(self)
    
    @property
    def Fv(self):
        from marketsim.gen._out.strategy.side._fv import Fv
        return Fv(self)
    
    pass
FundamentalValue = FundamentalValue_FloatIOrderBook
