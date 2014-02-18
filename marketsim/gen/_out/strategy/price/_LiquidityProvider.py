from marketsim.ops._all import Observable
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._ifunction import IFunctionSide
from marketsim import registry
from marketsim import context
@registry.expose(["Price function", "LiquidityProvider"])
class LiquidityProvider_SideFloatFloatIOrderBook(Observable[float]):
    """ 
    """ 
    def __init__(self, side = None, initialValue = None, priceDistr = None, book = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.math.random._lognormvariate import lognormvariate_FloatFloat as _math_random_lognormvariate_FloatFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import event
        Observable[float].__init__(self)
        self.side = side if side is not None else _side_Sell_()
        self.initialValue = initialValue if initialValue is not None else 100.0
        self.priceDistr = priceDistr if priceDistr is not None else _math_random_lognormvariate_FloatFloat(0.0,0.1)
        self.book = book if book is not None else _orderbook_OfTrader_IAccount()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunctionSide,
        'initialValue' : float,
        'priceDistr' : IFunctionfloat,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "LiquidityProvider(%(side)s, %(initialValue)s, %(priceDistr)s, %(book)s)" % self.__dict__
    
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
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatFloat as _ops_Mul_IObservableFloatFloat
        from marketsim.gen._out.orderbook._safesideprice import SafeSidePrice_IOrderQueueFloat as _orderbook_SafeSidePrice_IOrderQueueFloat
        from marketsim.gen._out.orderbook._queue import Queue_IOrderBookSide as _orderbook_Queue_IOrderBookSide
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        return _ops_Mul_IObservableFloatFloat(_orderbook_SafeSidePrice_IOrderQueueFloat(_orderbook_Queue_IOrderBookSide(self.book,self.side),_constant_Float(self.initialValue)),self.priceDistr)
    
def LiquidityProvider(side = None,initialValue = None,priceDistr = None,book = None): 
    from marketsim.gen._out._ifunction import IFunctionSide
    from marketsim.gen._out._ifunction import IFunctionfloat
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunctionSide):
        if initialValue is None or rtti.can_be_casted(initialValue, float):
            if priceDistr is None or rtti.can_be_casted(priceDistr, IFunctionfloat):
                if book is None or rtti.can_be_casted(book, IOrderBook):
                    return LiquidityProvider_SideFloatFloatIOrderBook(side,initialValue,priceDistr,book)
    raise Exception('Cannot find suitable overload for LiquidityProvider('+str(side) +':'+ str(type(side))+','+str(initialValue) +':'+ str(type(initialValue))+','+str(priceDistr) +':'+ str(type(priceDistr))+','+str(book) +':'+ str(type(book))+')')
