from marketsim import registry
from marketsim import Price
from marketsim.ops._function import Function
from marketsim.gen._intrinsic.orderbook.props import _TickSize_Impl
from marketsim import IOrderBook
@registry.expose(["Asset", "TickSize"])
class TickSize_Optional__IOrderBook_(Function[Price], _TickSize_Impl):
    """ 
    """ 
    def __init__(self, book = None):
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim import rtti
        self.book = book if book is not None else _orderbook_OfTrader()
        rtti.check_fields(self)
        _TickSize_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    def __repr__(self):
        return "TickSize(%(book)s)" % self.__dict__
    
TickSize = TickSize_Optional__IOrderBook_
