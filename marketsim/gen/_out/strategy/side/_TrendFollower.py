from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import context
@registry.expose(["Side function", "TrendFollower"])
class TrendFollower_FloatFloatIOrderBook(IFunctionSide):
    """ 
    """ 
    def __init__(self, alpha = None, threshold = None, book = None):
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import call
        from marketsim import rtti
        self.alpha = alpha if alpha is not None else 0.15
        self.threshold = threshold if threshold is not None else 0.0
        self.book = book if book is not None else call(_orderbook_OfTrader_IAccount,)
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float,
        'threshold' : float,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "TrendFollower(%(alpha)s, %(threshold)s, %(book)s)" % self.__dict__
    
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
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.math.ew._avg import Avg_IObservableFloatFloat as _math_EW_Avg_IObservableFloatFloat
        from marketsim import call
        from marketsim.gen._out.math._derivative import Derivative_IDifferentiable as _math_Derivative_IDifferentiable
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        return call(_strategy_side_Signal_FloatFloat,call(_math_Derivative_IDifferentiable,call(_math_EW_Avg_IObservableFloatFloat,call(_orderbook_MidPrice_IOrderBook,self.book),self.alpha)),self.threshold)
    
def TrendFollower(alpha = None,threshold = None,book = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim import rtti
    if alpha is None or rtti.can_be_casted(alpha, float):
        if threshold is None or rtti.can_be_casted(threshold, float):
            if book is None or rtti.can_be_casted(book, IOrderBook):
                return TrendFollower_FloatFloatIOrderBook(alpha,threshold,book)
    raise Exception('Cannot find suitable overload for TrendFollower('+str(alpha) +':'+ str(type(alpha))+','+str(threshold) +':'+ str(type(threshold))+','+str(book) +':'+ str(type(book))+')')
