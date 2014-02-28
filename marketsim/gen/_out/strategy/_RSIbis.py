from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
@registry.expose(["Strategy", "RSIbis"])
class RSIbis_IEventSideIObservableIOrderFloatFloatFloat(ISingleAssetStrategy):
    """   and starts to buy when RSI is greater than 50 + *threshold*
      and sells when RSI is less than 50 - *thresold*
    """ 
    def __init__(self, eventGen = None, orderFactory = None, alpha = None, timeframe = None, threshold = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import event
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float(deref_opt(_math_random_expovariate_Float(1.0))))
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_side_Market_Float())
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
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSide,
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
        from marketsim import deref_opt
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.strategy.side._signal import Signal_FloatFloat as _strategy_side_Signal_FloatFloat
        from marketsim.gen._out.ops._sub import Sub_FloatFloat as _ops_Sub_FloatFloat
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(self.orderFactory(deref_opt(_strategy_side_Signal_FloatFloat(deref_opt(_ops_Sub_FloatFloat(deref_opt(_constant_Float(50.0)),deref_opt(_math_RSI_IOrderBookFloatFloat(deref_opt(_orderbook_OfTrader_IAccount()),self.timeframe,self.alpha)))),(50.0-self.threshold))))),self.eventGen))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def RSIbis(eventGen = None,orderFactory = None,alpha = None,timeframe = None,threshold = None): 
    from marketsim.gen._out._ievent import IEvent
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
    from marketsim import rtti
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSide):
            if alpha is None or rtti.can_be_casted(alpha, float):
                if timeframe is None or rtti.can_be_casted(timeframe, float):
                    if threshold is None or rtti.can_be_casted(threshold, float):
                        return RSIbis_IEventSideIObservableIOrderFloatFloatFloat(eventGen,orderFactory,alpha,timeframe,threshold)
    raise Exception('Cannot find suitable overload for RSIbis('+str(eventGen) +':'+ str(type(eventGen))+','+str(orderFactory) +':'+ str(type(orderFactory))+','+str(alpha) +':'+ str(type(alpha))+','+str(timeframe) +':'+ str(type(timeframe))+','+str(threshold) +':'+ str(type(threshold))+')')
