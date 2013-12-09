from marketsim import registry
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.orderbook.queue import _Bids_Impl
from marketsim import IOrderBook
@registry.expose(['-', 'Bids'])
class Bids(Function[float]):
    """ 
    """ 
    def __init__(self, book = None):
        from marketsim.gen._out.observable.orderbook import OfTrader
        self.book = book if book is not None else OfTrader()
        _Bids_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    def __repr__(self):
        return "Bids" % self.__dict__
    
