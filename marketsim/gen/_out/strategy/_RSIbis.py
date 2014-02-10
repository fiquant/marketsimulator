from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import ISingleAssetStrategy
from marketsim import Side
from marketsim import registry
from marketsim import IEvent
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "RSIbis"])
class RSIbis_IEventSideIOrderGeneratorFloatFloatFloat(ISingleAssetStrategy):
    """   and starts to buy when RSI is greater than 50 + *threshold*
      and sells when RSI is less than 50 - *thresold*
    """ 
    def __init__(self, eventGen = None, orderFactory = None, alpha = None, timeframe = None, threshold = None):
        from marketsim.gen._out.order._curried._side_market import side_Market as _order__curried_side_Market
        from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        from marketsim.gen._out.event._every import Every as _event_Every
        self.eventGen = eventGen if eventGen is not None else _event_Every(_math_random_expovariate(1.0))
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market()
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
        'orderFactory' : IFunction[IOrderGenerator,IFunction[Side]],
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
        from marketsim.gen._out.ops._sub import Sub as _ops_Sub
        from marketsim.gen._out.orderbook._oftrader import OfTrader as _orderbook_OfTrader
        from marketsim.gen._out.math._rsi import RSI as _math_RSI
        from marketsim.gen._out.strategy._generic import Generic as _strategy_Generic
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.strategy.side._signal import Signal as _strategy_side_Signal
        return _strategy_Generic(self.orderFactory(_strategy_side_Signal(_ops_Sub(_constant(50.0),_math_RSI(_orderbook_OfTrader(),self.timeframe,self.alpha)),(50.0-self.threshold))),self.eventGen)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def RSIbis(eventGen = None,orderFactory = None,alpha = None,timeframe = None,threshold = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IEvent
    from marketsim import IOrderGenerator
    from marketsim import Side
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunction[IOrderGenerator,IFunction[Side]]):
            if alpha is None or rtti.can_be_casted(alpha, float):
                if timeframe is None or rtti.can_be_casted(timeframe, float):
                    if threshold is None or rtti.can_be_casted(threshold, float):
                        return RSIbis_IEventSideIOrderGeneratorFloatFloatFloat(eventGen,orderFactory,alpha,timeframe,threshold)
    raise Exception("Cannot find suitable overload")
