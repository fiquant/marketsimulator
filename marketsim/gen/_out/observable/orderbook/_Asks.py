from marketsim import registry
from marketsim.gen._intrinsic.orderbook.queue import _Asks_Impl
from marketsim import IOrderBook
@registry.expose(["Asset's", "Asks"])
class Asks(_Asks_Impl):
    """ 
    """ 
    def __init__(self, book = None):
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader as _observable_orderbook_OfTrader
        self.book = book if book is not None else _observable_orderbook_OfTrader()
        _Asks_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    def __repr__(self):
        return "Asks(%(book)s)" % self.__dict__
    
