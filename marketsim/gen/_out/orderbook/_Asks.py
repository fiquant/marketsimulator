from marketsim import registry
from marketsim.gen._intrinsic.orderbook.proxy import _Asks_Impl
from marketsim import IOrderBook
@registry.expose(["Asset", "Asks"])
class Asks(_Asks_Impl):""" 
    """ 
    def __init__(self, book = None):from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim import rtti
        self.book = book if book is not None else _orderbook_OfTrader()
        rtti.check_fields(self)
        _Asks_Impl.__init__(self)
    
    @property
    def label(self):return repr(self)
    
    _properties = {'book' : IOrderBook
    }
    def __repr__(self):return "Asks(%(book)s)" % self.__dict__
    
