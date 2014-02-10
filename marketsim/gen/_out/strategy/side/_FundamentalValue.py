from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IOrderBook
from marketsim import Side
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Side function", "FundamentalValue"])
class FundamentalValue_IFunctionFloatIOrderBook(Observable[Side]):
    """ 
    """ 
    def __init__(self, fv = None, book = None):
        from marketsim import Side
        from marketsim.gen._out.orderbook._oftrader import OfTrader as _orderbook_OfTrader
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out._constant import constant as _constant
        Observable[Side].__init__(self)
        self.fv = fv if fv is not None else _constant(200.0)
        self.book = book if book is not None else _orderbook_OfTrader()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'fv' : IFunction[float],
        'book' : IOrderBook
    }
    def __repr__(self):
        return "FundamentalValue(%(fv)s, %(book)s)" % self.__dict__
    
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
        from marketsim.gen._out.orderbook.ask._price import Price as _orderbook_ask_Price
        from marketsim.gen._out.side._nothing import Nothing as _side_Nothing
        from marketsim.gen._out.side._sell import Sell as _side_Sell
        from marketsim.gen._out.side._buy import Buy as _side_Buy
        from marketsim.gen._out.orderbook.bid._price import Price as _orderbook_bid_Price
        from marketsim.gen._out.ops._condition_side import Condition_Side as _ops_Condition_Side
        from marketsim.gen._out.ops._less import Less as _ops_Less
        from marketsim.gen._out.ops._greater import Greater as _ops_Greater
        return _ops_Condition_Side(_ops_Greater(_orderbook_bid_Price(self.book),self.fv),_side_Sell(),_ops_Condition_Side(_ops_Less(_orderbook_ask_Price(self.book),self.fv),_side_Buy(),_side_Nothing()))
    
def FundamentalValue(fv = None,book = None): 
    from marketsim import IFunction
    from marketsim import float
    from marketsim import IOrderBook
    from marketsim import rtti
    if fv is None or rtti.can_be_casted(fv, IFunction[float]):
        if book is None or rtti.can_be_casted(book, IOrderBook):
            return FundamentalValue_IFunctionFloatIOrderBook(fv,book)
    raise Exception("Cannot find suitable overload")
