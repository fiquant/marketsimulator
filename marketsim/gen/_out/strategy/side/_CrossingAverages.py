from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import context
@registry.expose(["Side function", "CrossingAverages"])
class CrossingAverages_FloatFloatFloatIOrderBook(IFunctionSide):
    """ 
    """ 
    def __init__(self, alpha_1 = None, alpha_2 = None, threshold = None, book = None):
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import deref_opt
        from marketsim import rtti
        self.alpha_1 = alpha_1 if alpha_1 is not None else 0.15
        self.alpha_2 = alpha_2 if alpha_2 is not None else 0.015
        self.threshold = threshold if threshold is not None else 0.0
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha_1' : float,
        'alpha_2' : float,
        'threshold' : float,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "CrossingAverages(%(alpha_1)s, %(alpha_2)s, %(threshold)s, %(book)s)" % self.__dict__
    
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
        from marketsim.gen._out.math._avg import Avg_mathEW as _math_Avg_mathEW
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.math._ew import EW_IObservableFloatFloat as _math_EW_IObservableFloatFloat
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        from marketsim.gen._out.ops._sub import Sub_FloatFloat as _ops_Sub_FloatFloat
        return deref_opt(_strategy_side_Signal_FloatFloat(deref_opt(_ops_Sub_FloatFloat(deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(self.book)),self.alpha_1)))),deref_opt(_math_Avg_mathEW(deref_opt(_math_EW_IObservableFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(self.book)),self.alpha_2)))))),self.threshold))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
def CrossingAverages(alpha_1 = None,alpha_2 = None,threshold = None,book = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim import rtti
    if alpha_1 is None or rtti.can_be_casted(alpha_1, float):
        if alpha_2 is None or rtti.can_be_casted(alpha_2, float):
            if threshold is None or rtti.can_be_casted(threshold, float):
                if book is None or rtti.can_be_casted(book, IOrderBook):
                    return CrossingAverages_FloatFloatFloatIOrderBook(alpha_1,alpha_2,threshold,book)
    raise Exception('Cannot find suitable overload for CrossingAverages('+str(alpha_1) +':'+ str(type(alpha_1))+','+str(alpha_2) +':'+ str(type(alpha_2))+','+str(threshold) +':'+ str(type(threshold))+','+str(book) +':'+ str(type(book))+')')
