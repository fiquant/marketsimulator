from marketsim import registry
from marketsim.gen._intrinsic.orderbook.queue import _Queue_Impl
from marketsim import IOrderBook
from marketsim import IFunction
from marketsim import Side
@registry.expose(["Asset's", "Queue"])
class Queue(_Queue_Impl):
    """ 
    """ 
    def __init__(self, book = None, side = None):
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        from marketsim.gen._out.side._Sell import Sell
        self.book = book if book is not None else OfTrader()
        self.side = side if side is not None else Sell()
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
    
