from marketsim import registry
from marketsim import Side
from marketsim.ops._all import Observable
from marketsim import IOrderBook
from marketsim import IOrderBook
from marketsim import context
@registry.expose(["Side function", "PairTrading"])
class PairTrading(Observable[Side]):
    """ 
    """ 
    def __init__(self, bookToDependOn = None, factor = None, book = None):
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim import rtti
        from marketsim import _
        from marketsim import event
        Observable[Side].__init__(self)
        self.bookToDependOn = bookToDependOn if bookToDependOn is not None else _orderbook_OfTrader()
        self.factor = factor if factor is not None else 1.0
        self.book = book if book is not None else _orderbook_OfTrader()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'bookToDependOn' : IOrderBook,
        'factor' : float,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "PairTrading(%(bookToDependOn)s, %(factor)s, %(book)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.observable._Side import Side as _observable_Side
        from marketsim.gen._out.strategy.side._FundamentalValue import FundamentalValue as _strategy_side_FundamentalValue
        from marketsim.gen._out.orderbook._MidPrice import MidPrice as _orderbook_MidPrice
        from marketsim.gen._out._const import const as _const
        return _observable_Side(_strategy_side_FundamentalValue(_orderbook_MidPrice(self.bookToDependOn)*_const(self.factor),self.book))
        
        
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
