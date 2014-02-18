from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
@registry.expose(["Strategy", "RSIbis"])
class RSIbis_IEventSideIObservableIOrderFloatFloatFloat(ISingleAssetStrategy):
    """   and starts to buy when RSI is greater than 50 + *threshold*
      and sells when RSI is less than 50 - *thresold*
    """ 
    def __init__(self, eventGen = None, orderFactory = None, alpha = None, timeframe = None, threshold = None):
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import event
        self.eventGen = eventGen if eventGen is not None else _event_Every_Float(_math_random_expovariate_Float(1.0))
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market_Float()
        self.alpha = alpha if alpha is not None else (1.0/14)
        self.timeframe = timeframe if timeframe is not None else 1.0
        self.threshold = threshold if threshold is not None else 30.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrderIFunctionSide,
        'alpha' : float,
        'timeframe' : float,
        'threshold' : float
    }
    def __repr__(self):
        return "RSIbis(%(eventGen)s, %(orderFactory)s, %(alpha)s, %(timeframe)s, %(threshold)s)" % self.__dict__
    
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
        from marketsim.gen._out.math._rsi import RSI_IOrderBookFloatFloat as _math_RSI_IOrderBookFloatFloat
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        from marketsim.gen._out.ops._sub import Sub_FloatFloat as _ops_Sub_FloatFloat
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        return _strategy_Generic_IObservableIOrderIEvent(self.orderFactory(_strategy_side_Signal_FloatFloat(_ops_Sub_FloatFloat(_constant_Float(50.0),_math_RSI_IOrderBookFloatFloat(_orderbook_OfTrader_IAccount(),self.timeframe,self.alpha)),(50.0-self.threshold))),self.eventGen)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def RSIbis(eventGen = None,orderFactory = None,alpha = None,timeframe = None,threshold = None): 
    from marketsim.gen._out._ievent import IEvent
    from marketsim.gen._out._ifunction import IFunctionIObservableIOrderIFunctionSide
    from marketsim import rtti
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrderIFunctionSide):
            if alpha is None or rtti.can_be_casted(alpha, float):
                if timeframe is None or rtti.can_be_casted(timeframe, float):
                    if threshold is None or rtti.can_be_casted(threshold, float):
                        return RSIbis_IEventSideIObservableIOrderFloatFloatFloat(eventGen,orderFactory,alpha,timeframe,threshold)
    raise Exception('Cannot find suitable overload for RSIbis('+str(eventGen) +':'+ str(type(eventGen))+','+str(orderFactory) +':'+ str(type(orderFactory))+','+str(alpha) +':'+ str(type(alpha))+','+str(timeframe) +':'+ str(type(timeframe))+','+str(threshold) +':'+ str(type(threshold))+')')
