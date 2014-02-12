from marketsim.ops._all import Observable
from marketsim import IOrderBook
from marketsim import registry
from marketsim import Price
from marketsim import context
@registry.expose(["Asset", "Spread"])
class Spread_IOrderBook(Observable[Price]):
    """ 
    """ 
    def __init__(self, book = None):
        from marketsim import Price
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import event
        Observable[Price].__init__(self)
        self.book = book if book is not None else _orderbook_OfTrader_IAccount()
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
        return "Spread(%(book)s)" % self.__dict__
    
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
        from marketsim.gen._out.observable._price import Price_IFunctionFloat as _observable_Price_IFunctionFloat
        from marketsim.gen._out.ops._sub import Sub_IObservableFloatIObservableFloat as _ops_Sub_IObservableFloatIObservableFloat
        from marketsim.gen._out.orderbook.ask._price import Price_IOrderBook as _orderbook_ask_Price_IOrderBook
        from marketsim.gen._out.orderbook.bid._price import Price_IOrderBook as _orderbook_bid_Price_IOrderBook
        return _observable_Price_IFunctionFloat(_ops_Sub_IObservableFloatIObservableFloat(_orderbook_ask_Price_IOrderBook(self.book),_orderbook_bid_Price_IOrderBook(self.book)))
    
def Spread(book = None): 
    from marketsim import IOrderBook
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        return Spread_IOrderBook(book)
    raise Exception('Cannot find suitable overload for Spread('+str(book)+')')
