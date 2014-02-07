from marketsim.ops._all import Observable
from marketsim import IOrderBook
from marketsim import Side
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Side function", "PairTrading"])
class PairTrading_Optional__IOrderBook___Optional__Float___Optional__IOrderBook_(Observable[Side]):
    """ 
    """ 
    def __init__(self, bookToDependOn = None, factor = None, book = None):
        from marketsim import Side
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
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
        from marketsim.gen._out.ops._Mul import Mul as _ops_Mul
        from marketsim.gen._out.orderbook._MidPrice import MidPrice as _orderbook_MidPrice
        from marketsim.gen._out.strategy.side._FundamentalValue import FundamentalValue as _strategy_side_FundamentalValue
        from marketsim.gen._out.observable._Side import Side as _observable_Side
        return _observable_Side(_strategy_side_FundamentalValue(_ops_Mul(_orderbook_MidPrice(self.bookToDependOn),_const(self.factor)),self.book))
    
def PairTrading(bookToDependOn = None,factor = None,book = None): 
    from marketsim import IOrderBook
    from marketsim import float
    from marketsim import rtti
    if bookToDependOn is None or rtti.can_be_casted(bookToDependOn, IOrderBook):
        if factor is None or rtti.can_be_casted(factor, float):
            if book is None or rtti.can_be_casted(book, IOrderBook):
                return PairTrading_Optional__IOrderBook___Optional__Float___Optional__IOrderBook_(bookToDependOn,factor,book)
    raise Exception("Cannot find suitable overload")
