from marketsim.ops._all import Observable
from marketsim.gen._intrinsic.orderbook.cumulative_price import CumulativePrice_Impl
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import registry
@registry.expose(["Asset", "CumulativePrice"])
class CumulativePrice_IOrderBookFloat(Observable[float],CumulativePrice_Impl):
    """ 
      In other words cumulative price corresponds to trader balance change
      if a market order of volume *depth* is completely matched
    
      Negative *depth* correponds to will buy assets
      Positive *depth* correponds to will sell assets
    """ 
    def __init__(self, book = None, depth = None):
        from marketsim.ops._all import Observable
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import rtti
        Observable[float].__init__(self)
        self.book = book if book is not None else _orderbook_OfTrader_IAccount()
        
        self.depth = depth if depth is not None else _constant_Float(1.0)
        
        rtti.check_fields(self)
        CumulativePrice_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'depth' : IFunctionfloat
    }
    def __repr__(self):
        return "CumulativePrice(%(book)s, %(depth)s)" % self.__dict__
    
def CumulativePrice(book = None,depth = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if depth is None or rtti.can_be_casted(depth, IFunctionfloat):
            return CumulativePrice_IOrderBookFloat(book,depth)
    raise Exception('Cannot find suitable overload for CumulativePrice('+str(book) +':'+ str(type(book))+','+str(depth) +':'+ str(type(depth))+')')
