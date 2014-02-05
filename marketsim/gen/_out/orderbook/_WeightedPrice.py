from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim import IOrderQueue
from marketsim import float
from marketsim import context
@registry.expose(["Asset", "WeightedPrice"])
class WeightedPrice_Optional__IOrderQueue___Optional__Float_(Function[float]):
    """ 
    """ 
    def __init__(self, queue = None, alpha = None):
        from marketsim.gen._out.orderbook._Asks import Asks as _orderbook_Asks
        from marketsim import rtti
        self.queue = queue if queue is not None else _orderbook_Asks()
        self.alpha = alpha if alpha is not None else 0.15
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'queue' : IOrderQueue,
        'alpha' : float
    }
    def __repr__(self):
        return "Price_{%(alpha)s}^{%(queue)s}" % self.__dict__
    
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
        from marketsim.gen._out.ops._Div import Div as _ops_Div
        from marketsim.gen._out.math.EW._Avg import Avg as _math_EW_Avg
        from marketsim.gen._out.observable._Float import Float as _observable_Float
        from marketsim.gen._out.ops._Mul import Mul as _ops_Mul
        from marketsim.gen._out.orderbook._LastTradePrice import LastTradePrice as _orderbook_LastTradePrice
        from marketsim.gen._out.orderbook._LastTradeVolume import LastTradeVolume as _orderbook_LastTradeVolume
        from marketsim.gen._out.math.EW._Avg import Avg as _math_EW_Avg
        from marketsim.gen._out.orderbook._LastTradeVolume import LastTradeVolume as _orderbook_LastTradeVolume
        return _ops_Div(_math_EW_Avg(_observable_Float(_ops_Mul(_orderbook_LastTradePrice(self.queue),_orderbook_LastTradeVolume(self.queue))),self.alpha),_math_EW_Avg(_orderbook_LastTradeVolume(self.queue),self.alpha))
    
WeightedPrice = WeightedPrice_Optional__IOrderQueue___Optional__Float_
