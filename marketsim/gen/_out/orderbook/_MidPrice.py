from marketsim.ops._all import Observable
from marketsim import IOrderBook
from marketsim import registry
from marketsim import Price
from marketsim import context
@registry.expose(["Asset", "MidPrice"])
class MidPrice_Optional__IOrderBook_(Observable[Price]):
    """ 
    """ 
    def __init__(self, book = None):
        from marketsim import Price
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        Observable[Price].__init__(self)
        self.book = book if book is not None else _orderbook_OfTrader()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook
    }
    def __repr__(self):
        return "MidPrice(%(book)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.orderbook.ask._Price import Price as _orderbook_ask_Price
        from marketsim.gen._out.orderbook.bid._Price import Price as _orderbook_bid_Price
        from marketsim.gen._out.ops._Add import Add as _ops_Add
        from marketsim.gen._out.ops._Div import Div as _ops_Div
        from marketsim.gen._out.observable._Price import Price as _observable_Price
        return _observable_Price(_ops_Div(_ops_Add(_orderbook_ask_Price(self.book),_orderbook_bid_Price(self.book)),_const(2.0)))
    
def MidPrice(book = None): 
    return MidPrice_Optional__IOrderBook_(book)
