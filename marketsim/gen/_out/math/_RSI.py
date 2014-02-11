from marketsim import IOrderBook
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import context
from marketsim import float
@registry.expose(["Basic", "RSI"])
class RSI_IOrderBookFloatFloat(Function[float]):
    """ 
    """ 
    def __init__(self, book = None, timeframe = None, alpha = None):
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader
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
        from marketsim.gen._out.ops._div import Div_IFunctionFloatIFunctionFloat as _ops_Div
        from marketsim.gen._out.orderbook._midprice import MidPrice_IOrderBook as _orderbook_MidPrice
        from marketsim.gen._out.math.rsi._raw import Raw_IObservableFloatFloatFloat as _math_rsi_Raw
        from marketsim.gen._out.ops._sub import Sub_IFunctionFloatIFunctionFloat as _ops_Sub
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim.gen._out.ops._add import Add_IFunctionFloatIFunctionFloat as _ops_Add
        return _ops_Sub(_constant(100.0),_ops_Div(_constant(100.0),_ops_Add(_constant(1.0),_math_rsi_Raw(_orderbook_MidPrice(self.book),self.timeframe,self.alpha))))
    
def RSI(book = None,timeframe = None,alpha = None): 
    from marketsim import IOrderBook
    from marketsim import float
    from marketsim import rtti
    if book is None or rtti.can_be_casted(book, IOrderBook):
        if timeframe is None or rtti.can_be_casted(timeframe, float):
            if alpha is None or rtti.can_be_casted(alpha, float):
                return RSI_IOrderBookFloatFloat(book,timeframe,alpha)
    raise Exception('Cannot find suitable overload for RSI('+str(book)+','+str(timeframe)+','+str(alpha)+')')
