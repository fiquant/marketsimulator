from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import IOrderBook
from marketsim import Side
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Side function", "FundamentalValue"])
class FundamentalValue_IObservableFloatIOrderBook(Observable[Side]):
    """ 
    """ 
    def __init__(self, fv = None, book = None):
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[Side].__init__(self)
        self.fv = fv if fv is not None else _const_Float(200.0)
        self.book = book if book is not None else _orderbook_OfTrader_IAccount()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'fv' : IObservable[float],
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
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._greater import Greater_IFunctionFloatIFunctionFloat as _ops_Greater_IFunctionFloatIFunctionFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.ops._less import Less_IFunctionFloatIFunctionFloat as _ops_Less_IFunctionFloatIFunctionFloat
        from marketsim.gen._out.orderbook.ask._price import Price_IOrderBook as _orderbook_ask_Price_IOrderBook
        from marketsim.gen._out.ops._condition import Condition_IFunctionBooleanSideSide as _ops_Condition_IFunctionBooleanSideSide
        from marketsim.gen._out.orderbook.bid._price import Price_IOrderBook as _orderbook_bid_Price_IOrderBook
        return _ops_Condition_IFunctionBooleanSideSide(_ops_Greater_IFunctionFloatIFunctionFloat(_orderbook_bid_Price_IOrderBook(self.book),self.fv),_side_Sell_(),_ops_Condition_IFunctionBooleanSideSide(_ops_Less_IFunctionFloatIFunctionFloat(_orderbook_ask_Price_IOrderBook(self.book),self.fv),_side_Buy_(),_side_Nothing_()))
    
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
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        Observable[Side].__init__(self)
        self.fv = fv if fv is not None else _constant_Float(200.0)
        self.book = book if book is not None else _orderbook_OfTrader_IAccount()
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
        from marketsim.gen._out.side._nothing import Nothing_ as _side_Nothing_
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.ops._greater import Greater_IFunctionFloatIFunctionFloat as _ops_Greater_IFunctionFloatIFunctionFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.ops._less import Less_IFunctionFloatIFunctionFloat as _ops_Less_IFunctionFloatIFunctionFloat
        from marketsim.gen._out.orderbook.ask._price import Price_IOrderBook as _orderbook_ask_Price_IOrderBook
        from marketsim.gen._out.ops._condition import Condition_IFunctionBooleanSideSide as _ops_Condition_IFunctionBooleanSideSide
        from marketsim.gen._out.orderbook.bid._price import Price_IOrderBook as _orderbook_bid_Price_IOrderBook
        return _ops_Condition_IFunctionBooleanSideSide(_ops_Greater_IFunctionFloatIFunctionFloat(_orderbook_bid_Price_IOrderBook(self.book),self.fv),_side_Sell_(),_ops_Condition_IFunctionBooleanSideSide(_ops_Less_IFunctionFloatIFunctionFloat(_orderbook_ask_Price_IOrderBook(self.book),self.fv),_side_Buy_(),_side_Nothing_()))
    
def FundamentalValue(fv = None,book = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IOrderBook
    if fv is None or rtti.can_be_casted(fv, IObservable[float]):
        if book is None or rtti.can_be_casted(book, IOrderBook):
            return FundamentalValue_IObservableFloatIOrderBook(fv,book)
    if fv is None or rtti.can_be_casted(fv, IFunction[float]):
        if book is None or rtti.can_be_casted(book, IOrderBook):
            return FundamentalValue_IFunctionFloatIOrderBook(fv,book)
    raise Exception('Cannot find suitable overload for FundamentalValue('+str(fv)+','+str(book)+')')
