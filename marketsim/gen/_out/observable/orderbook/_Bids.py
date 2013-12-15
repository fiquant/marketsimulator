from marketsim import registry
from marketsim.gen._intrinsic.orderbook.queue import _Bids_Impl
from marketsim import IOrderBook
@registry.expose(["Asset's", "Bids"])
class Bids(_Bids_Impl):
    """ 
    """ 
    def __init__(self, book = None):
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        self.book = book if book is not None else OfTrader()
        _Bids_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    def __repr__(self):
        return "Bids(%(book)s)" % self.__dict__
    
