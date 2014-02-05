from marketsim import registry
from marketsim.gen._intrinsic.orderbook.cumulative_price import CumulativePrice_Impl
from marketsim import IOrderBook
from marketsim import IFunction
from marketsim import float
@registry.expose(["Asset", "CumulativePrice"])
class CumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__(CumulativePrice_Impl):
    """ 
      In other words cumulative price corresponds to trader balance change
      if a market order of volume *depth* is completely matched
    
      Negative *depth* correponds to will buy assets
      Positive *depth* correponds to will sell assets
    """ 
    def __init__(self, book = None, depth = None):
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        self.book = book if book is not None else _orderbook_OfTrader()
        if isinstance(book, types.IEvent):
            event.subscribe(self.book, self.fire, self)
        self.depth = depth if depth is not None else _constant()
        if isinstance(depth, types.IEvent):
            event.subscribe(self.depth, self.fire, self)
        rtti.check_fields(self)
        CumulativePrice_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'depth' : IFunction[float]
    }
    def __repr__(self):
        return "CumulativePrice(%(book)s, %(depth)s)" % self.__dict__
    
CumulativePrice = CumulativePrice_Optional__IOrderBook___Optional__IFunction__Float__
