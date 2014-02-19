from marketsim.gen._out._side import Side
from marketsim.gen._out._observable import ObservableSide
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import registry
from marketsim import context
@registry.expose(["Side function", "MeanReversion"])
class MeanReversion_FloatIOrderBook(ObservableSide):
    """ 
    """ 
    def __init__(self, alpha = None, book = None):
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._side import Side
        from marketsim import event
        from marketsim.gen._out._observable import ObservableSide
        ObservableSide.__init__(self)
        self.alpha = alpha if alpha is not None else 0.015
        self.book = book if book is not None else _orderbook_OfTrader_IAccount()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "MeanReversion(%(alpha)s, %(book)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_FloatIOrderBook as _strategy_side_FundamentalValue_FloatIOrderBook
        from marketsim.gen._out.math.EW._avg import Avg_IObservableFloatFloat as _math_EW_Avg_IObservableFloatFloat
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        return _strategy_side_FundamentalValue_FloatIOrderBook(_math_EW_Avg_IObservableFloatFloat(_orderbook_MidPrice_IOrderBook(self.book),self.alpha),self.book)
    
def MeanReversion(alpha = None,book = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim import rtti
    if alpha is None or rtti.can_be_casted(alpha, float):
        if book is None or rtti.can_be_casted(book, IOrderBook):
            return MeanReversion_FloatIOrderBook(alpha,book)
    raise Exception('Cannot find suitable overload for MeanReversion('+str(alpha) +':'+ str(type(alpha))+','+str(book) +':'+ str(type(book))+')')
