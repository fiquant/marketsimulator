from marketsim.ops._all import Observable
from marketsim.gen._out._side import Side
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import registry
from marketsim import context
@registry.expose(["Side function", "PairTrading"])
class PairTrading_IOrderBookFloatIOrderBook(Observable[Side]):
    """ 
    """ 
    def __init__(self, bookToDependOn = None, factor = None, book = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._side import Side
        from marketsim import event
        Observable[Side].__init__(self)
        self.bookToDependOn = bookToDependOn if bookToDependOn is not None else _orderbook_OfTrader_IAccount()
        self.factor = factor if factor is not None else 1.0
        self.book = book if book is not None else _orderbook_OfTrader_IAccount()
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
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_IObservableFloatIOrderBook as _strategy_side_FundamentalValue_IObservableFloatIOrderBook
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatFloat as _ops_Mul_IObservableFloatFloat
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        return _strategy_side_FundamentalValue_IObservableFloatIOrderBook(_ops_Mul_IObservableFloatFloat(_orderbook_MidPrice_IOrderBook(self.bookToDependOn),_constant_Float(self.factor)),self.book)
    
def PairTrading(bookToDependOn = None,factor = None,book = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim import rtti
    if bookToDependOn is None or rtti.can_be_casted(bookToDependOn, IOrderBook):
        if factor is None or rtti.can_be_casted(factor, float):
            if book is None or rtti.can_be_casted(book, IOrderBook):
                return PairTrading_IOrderBookFloatIOrderBook(bookToDependOn,factor,book)
    raise Exception('Cannot find suitable overload for PairTrading('+str(bookToDependOn) +':'+ str(type(bookToDependOn))+','+str(factor) +':'+ str(type(factor))+','+str(book) +':'+ str(type(book))+')')
