from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderBook
from marketsim import IOrderBook
from marketsim import context
@registry.expose(["Price function", "LiquidityProvider"])
class LiquidityProvider(Observable[float]):
    """ 
    """ 
    def __init__(self, side = None, initialValue = None, priceDistr = None, book = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out.math.random._lognormvariate import lognormvariate as _math_random_lognormvariate
        from marketsim.gen._out.math.random._lognormvariate import lognormvariate as _math_random_lognormvariate
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.side = side if side is not None else _side_Sell()
        self.initialValue = initialValue if initialValue is not None else 100.0
        self.priceDistr = priceDistr if priceDistr is not None else _math_random_lognormvariate(0.0,0.1)
        self.book = book if book is not None else _orderbook_OfTrader()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunction[Side]
        
        ,
        'initialValue' : float,
        'priceDistr' : IFunction[float],
        'book' : IOrderBook
    }
    def __repr__(self):
        return "LiquidityProvider(%(side)s, %(initialValue)s, %(priceDistr)s, %(book)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.orderbook._SafeSidePrice import SafeSidePrice as _orderbook_SafeSidePrice
        from marketsim.gen._out.orderbook._Queue import Queue as _orderbook_Queue
        from marketsim.gen._out._constant import constant as _constant
        return _orderbook_SafeSidePrice(_orderbook_Queue(self.book,self.side),_constant(self.initialValue))*self.priceDistr
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
