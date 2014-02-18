from marketsim import registry
from marketsim.gen._out._ifunction import IFunctionfloat
from marketsim.gen._out._iorderqueue import IOrderQueue
from marketsim import context
@registry.expose(["Asset", "WeightedPrice"])
class WeightedPrice_IOrderQueueFloat(IFunctionfloat):
    """ 
    """ 
    def __init__(self, queue = None, alpha = None):
        from marketsim.gen._out.orderbook._asks import Asks_IOrderBook as _orderbook_Asks_IOrderBook
        from marketsim import rtti
        self.queue = queue if queue is not None else _orderbook_Asks_IOrderBook()
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
        from marketsim.gen._out.orderbook._lasttradeprice import LastTradePrice_IOrderQueue as _orderbook_LastTradePrice_IOrderQueue
        from marketsim.gen._out.orderbook._lasttradevolume import LastTradeVolume_IOrderQueue as _orderbook_LastTradeVolume_IOrderQueue
        from marketsim.gen._out.ops._div import Div_FloatFloat as _ops_Div_FloatFloat
        from marketsim.gen._out.math.EW._avg import Avg_IObservableFloatFloat as _math_EW_Avg_IObservableFloatFloat
        from marketsim.gen._out.ops._mul import Mul_IObservableFloatIObservableFloat as _ops_Mul_IObservableFloatIObservableFloat
        return _ops_Div_FloatFloat(_math_EW_Avg_IObservableFloatFloat(_ops_Mul_IObservableFloatIObservableFloat(_orderbook_LastTradePrice_IOrderQueue(self.queue),_orderbook_LastTradeVolume_IOrderQueue(self.queue)),self.alpha),_math_EW_Avg_IObservableFloatFloat(_orderbook_LastTradeVolume_IOrderQueue(self.queue),self.alpha))
    
def WeightedPrice(queue = None,alpha = None): 
    from marketsim.gen._out._iorderqueue import IOrderQueue
    from marketsim import rtti
    if queue is None or rtti.can_be_casted(queue, IOrderQueue):
        if alpha is None or rtti.can_be_casted(alpha, float):
            return WeightedPrice_IOrderQueueFloat(queue,alpha)
    raise Exception('Cannot find suitable overload for WeightedPrice('+str(queue) +':'+ str(type(queue))+','+str(alpha) +':'+ str(type(alpha))+')')
