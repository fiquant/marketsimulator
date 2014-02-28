from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim import context
@registry.expose(["Basic", "RSI"])
class RSI_IOrderBookFloatFloat(IFunctionfloat):
    """ 
    """ 
    def __init__(self, book = None, timeframe = None, alpha = None):
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim import deref_opt
        from marketsim import rtti
        self.book = book if book is not None else deref_opt(_orderbook_OfTrader_IAccount())
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
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice_IOrderBook
        from marketsim.gen._out.ops._div import Div_FloatFloat as _ops_Div_FloatFloat
        from marketsim.gen._out.math.rsi._raw import Raw_IObservableFloatFloatFloat as _math_rsi_Raw_IObservableFloatFloatFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.ops._add import Add_FloatFloat as _ops_Add_FloatFloat
        from marketsim.gen._out.ops._sub import Sub_FloatFloat as _ops_Sub_FloatFloat
        return deref_opt(_ops_Sub_FloatFloat(deref_opt(_constant_Float(100.0)),deref_opt(_ops_Div_FloatFloat(deref_opt(_constant_Float(100.0)),deref_opt(_ops_Add_FloatFloat(deref_opt(_constant_Float(1.0)),deref_opt(_math_rsi_Raw_IObservableFloatFloatFloat(deref_opt(_orderbook_MidPrice_IOrderBook(self.book)),self.timeframe,self.alpha))))))))
    
def RSI(book = None,timeframe = None,alpha = None): 
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            if alpha is None or rtti.can_be_casted(alpha, float):
                return RSI_IOrderBookFloatFloat(book,timeframe,alpha)
    raise Exception('Cannot find suitable overload for RSI('+str(book) +':'+ str(type(book))+','+str(timeframe) +':'+ str(type(timeframe))+','+str(alpha) +':'+ str(type(alpha))+')')
