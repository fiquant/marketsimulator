from marketsim import registry
from marketsim.ops._function import Function
from marketsim import Price
from marketsim.gen._intrinsic.orderbook.props import _TickSize_Impl
from marketsim import IOrderBook
@registry.expose(["Asset's", "TickSize"])
class TickSize(Function[Price], _TickSize_Impl):
    """ 
    """ 
    def __init__(self, book = None):
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        self.book = book if book is not None else OfTrader()
        _TickSize_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    def __repr__(self):
        return "TickSize(%(book)s)" % self.__dict__
    
