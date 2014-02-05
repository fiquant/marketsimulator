from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim import IOrderBook
from marketsim import float
from marketsim import float
from marketsim import context
@registry.expose(["Basic", "RSI"])
class RSI_Optional__IOrderBook___Optional__Float___Optional__Float_(Function[float]):
    """ 
    """ 
    def __init__(self, book = None, timeframe = None, alpha = None):
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim import rtti
        self.book = book if book is not None else _orderbook_OfTrader()
        self.timeframe = timeframe if timeframe is not None else 10.0
        self.alpha = alpha if alpha is not None else 0.015
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'timeframe' : float,
        'alpha' : float
    }
    def __repr__(self):
        return "RSI_{%(timeframe)s}^{%(alpha)s}(%(book)s)" % self.__dict__
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.ops._Sub import Sub as _ops_Sub
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.ops._Div import Div as _ops_Div
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.ops._Add import Add as _ops_Add
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.math.rsi._Raw import Raw as _math_rsi_Raw
        from marketsim.gen._out.orderbook._MidPrice import MidPrice as _orderbook_MidPrice
        return _ops_Sub(_const(100.0),_ops_Div(_const(100.0),_ops_Add(_const(1.0),_math_rsi_Raw(_orderbook_MidPrice(self.book),self.timeframe,self.alpha))))
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
RSI = RSI_Optional__IOrderBook___Optional__Float___Optional__Float_
