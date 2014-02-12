from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim.gen._intrinsic.orderbook.cumulative_price import CumulativePrice_Impl
from marketsim import IOrderBook
from marketsim import registry
from marketsim import Price
from marketsim import float
@registry.expose(["Asset", "CumulativePrice"])
class CumulativePrice_IOrderBookIFunctionFloat(Observable[Price],CumulativePrice_Impl):
    """ 
      In other words cumulative price corresponds to trader balance change
      if a market order of volume *depth* is completely matched
    
      Negative *depth* correponds to will buy assets
      Positive *depth* correponds to will sell assets
    """ 
    def __init__(self, book = None, depth = None):
        from marketsim import Price
        from marketsim import types
        from marketsim.ops._all import Observable
        from marketsim import rtti
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        Observable[Price].__init__(self)
        self.book = book if book is not None else _orderbook_OfTrader_IAccount()
        if isinstance(book, types.IEvent):
            event.subscribe(self.book, self.fire, self)
        self.depth = depth if depth is not None else _constant_Float(1.0)
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
    
def CumulativePrice(book = None,depth = None): 
    from marketsim import IOrderBook
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if depth is None or rtti.can_be_casted(depth, IFunction[float]):
            return CumulativePrice_IOrderBookIFunctionFloat(book,depth)
    raise Exception('Cannot find suitable overload for CumulativePrice('+str(book)+','+str(depth)+')')
