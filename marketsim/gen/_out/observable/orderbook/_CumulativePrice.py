from marketsim import registry
from marketsim.gen._intrinsic.orderbook.cumulative_price import CumulativePrice_Impl
from marketsim import IOrderBook
from marketsim import IFunction_float
@registry.expose(["Asset's", "CumulativePrice"])
class CumulativePrice(CumulativePrice_Impl):
    """ 
    """ 
    def __init__(self, book = None, depth = None):
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        from marketsim.gen._out._constant import constant
        from marketsim import event
        from marketsim import types
        from marketsim import event
        from marketsim import types
        self.book = book if book is not None else OfTrader()
        self.depth = depth if depth is not None else constant()
        CumulativePrice_Impl.__init__(self)
        if isinstance(book, types.IEvent):
            event.subscribe(self.book, self.fire, self)
        if isinstance(depth, types.IEvent):
            event.subscribe(self.depth, self.fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'depth' : IFunction_float
    }
    def __repr__(self):
        return "CumulativePrice(%(book)s, %(depth)s)" % self.__dict__
    
