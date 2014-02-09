from marketsim import IFunction
from marketsim import IOrderBook
from marketsim import Side
from marketsim import registry
from marketsim.gen._intrinsic.orderbook.proxy import _Queue_Impl
@registry.expose(["Asset", "Queue"])
class Queue_IOrderBookSide(_Queue_Impl):
    """ 
    """ 
    def __init__(self, book = None, side = None):
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim import rtti
        self.book = book if book is not None else _orderbook_OfTrader()
        self.side = side if side is not None else _side_Sell()
        rtti.check_fields(self)
        _Queue_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'side' : IFunction[Side]
    }
    def __repr__(self):
        return "Queue(%(book)s, %(side)s)" % self.__dict__
    
def Queue(book = None,side = None): 
    from marketsim import IOrderBook
    from marketsim import Side
    from marketsim import IFunction
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if side is None or rtti.can_be_casted(side, IFunction[Side]):
            return Queue_IOrderBookSide(book,side)
    raise Exception("Cannot find suitable overload")
