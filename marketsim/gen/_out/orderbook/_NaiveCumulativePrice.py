from marketsim.ops._all import Observable
from marketsim import IObservable
from marketsim import IOrderBook
from marketsim import registry
from marketsim import Price
from marketsim import context
from marketsim import float
@registry.expose(["Asset", "NaiveCumulativePrice"])
class NaiveCumulativePrice_IOrderBookIObservableFloat(Observable[Price]):
    """   by taking into account prices only for the best order
    
      Negative *depth* correponds to will buy assets
      Positive *depth* correponds to will sell assets
    """ 
    def __init__(self, book = None, depth = None):
        from marketsim import Price
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        Observable[Price].__init__(self)
        self.book = book if book is not None else _orderbook_OfTrader_IAccount()
        self.depth = depth if depth is not None else _const_Float(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'depth' : IObservable[float]
    }
    def __repr__(self):
        return "NaiveCumulativePrice(%(book)s, %(depth)s)" % self.__dict__
    
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
        from marketsim.gen._out.ops._greater import Greater_IFunctionFloatIFunctionFloat as _ops_Greater_IFunctionFloatIFunctionFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.ops._condition_float import Condition_Float_IFunctionBooleanIFunctionFloatIFunctionFloat as _ops_Condition_Float_IFunctionBooleanIFunctionFloatIFunctionFloat
        from marketsim.gen._out.ops._less import Less_IFunctionFloatIFunctionFloat as _ops_Less_IFunctionFloatIFunctionFloat
        from marketsim.gen._out.orderbook.ask._price import Price_IOrderBook as _orderbook_ask_Price_IOrderBook
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatIObservableFloat as _ops_Mul_IObservableFloatIObservableFloat
        from marketsim.gen._out.orderbook.bid._price import Price_IOrderBook as _orderbook_bid_Price_IOrderBook
        return _observable_Price_IFunctionFloat(_ops_Condition_Float_IFunctionBooleanIFunctionFloatIFunctionFloat(_ops_Less_IFunctionFloatIFunctionFloat(self.depth,_constant_Float(0.0)),_ops_Mul_IObservableFloatIObservableFloat(self.depth,_orderbook_ask_Price_IOrderBook(self.book)),_ops_Condition_Float_IFunctionBooleanIFunctionFloatIFunctionFloat(_ops_Greater_IFunctionFloatIFunctionFloat(self.depth,_constant_Float(0.0)),_ops_Mul_IObservableFloatIObservableFloat(self.depth,_orderbook_bid_Price_IOrderBook(self.book)),_constant_Float(0.0))))
    
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import IOrderBook
from marketsim import registry
from marketsim import Price
from marketsim import context
from marketsim import float
@registry.expose(["Asset", "NaiveCumulativePrice"])
class NaiveCumulativePrice_IOrderBookIFunctionFloat(Observable[Price]):
    """   by taking into account prices only for the best order
    
      Negative *depth* correponds to will buy assets
      Positive *depth* correponds to will sell assets
    """ 
    def __init__(self, book = None, depth = None):
        from marketsim import Price
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import event
        Observable[Price].__init__(self)
        self.book = book if book is not None else _orderbook_OfTrader_IAccount()
        self.depth = depth if depth is not None else _constant_Float(1.0)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'depth' : IFunction[float]
    }
    def __repr__(self):
        return "NaiveCumulativePrice(%(book)s, %(depth)s)" % self.__dict__
    
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
        from marketsim.gen._out.ops._greater import Greater_IFunctionFloatIFunctionFloat as _ops_Greater_IFunctionFloatIFunctionFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.ops._condition_float import Condition_Float_IFunctionBooleanIFunctionFloatIFunctionFloat as _ops_Condition_Float_IFunctionBooleanIFunctionFloatIFunctionFloat
        from marketsim.gen._out.ops._less import Less_IFunctionFloatIFunctionFloat as _ops_Less_IFunctionFloatIFunctionFloat
        from marketsim.gen._out.ops._mul import Mul_IFunctionFloatIObservableFloat as _ops_Mul_IFunctionFloatIObservableFloat
        from marketsim.gen._out.orderbook.ask._price import Price_IOrderBook as _orderbook_ask_Price_IOrderBook
        from marketsim.gen._out.orderbook.bid._price import Price_IOrderBook as _orderbook_bid_Price_IOrderBook
        return _observable_Price_IFunctionFloat(_ops_Condition_Float_IFunctionBooleanIFunctionFloatIFunctionFloat(_ops_Less_IFunctionFloatIFunctionFloat(self.depth,_constant_Float(0.0)),_ops_Mul_IFunctionFloatIObservableFloat(self.depth,_orderbook_ask_Price_IOrderBook(self.book)),_ops_Condition_Float_IFunctionBooleanIFunctionFloatIFunctionFloat(_ops_Greater_IFunctionFloatIFunctionFloat(self.depth,_constant_Float(0.0)),_ops_Mul_IFunctionFloatIObservableFloat(self.depth,_orderbook_bid_Price_IOrderBook(self.book)),_constant_Float(0.0))))
    
def NaiveCumulativePrice(book = None,depth = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import IObservable
    from marketsim import float
    from marketsim import IOrderBook
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if depth is None or rtti.can_be_casted(depth, IObservable[float]):
            return NaiveCumulativePrice_IOrderBookIObservableFloat(book,depth)
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if depth is None or rtti.can_be_casted(depth, IFunction[float]):
            return NaiveCumulativePrice_IOrderBookIFunctionFloat(book,depth)
    raise Exception('Cannot find suitable overload for NaiveCumulativePrice('+str(book)+','+str(depth)+')')
