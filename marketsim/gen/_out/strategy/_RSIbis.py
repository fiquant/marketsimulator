from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim import IEvent
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
from marketsim import float
from marketsim import float
from marketsim import context
@registry.expose(["Strategy", "RSIbis"])
class RSIbis(ISingleAssetStrategy):
    """   and starts to buy when RSI is greater than 50 + *threshold*
      and sells when RSI is less than 50 - *thresold*
    """ 
    def __init__(self, eventGen = None, orderFactory = None, alpha = None, timeframe = None, threshold = None):
        from marketsim.gen._out.event._Every import Every as _event_Every
        from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim.gen._out.order._curried._side_Market import side_Market as _order__curried_side_Market
        from marketsim import rtti
        from marketsim import event
        from marketsim import _
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
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
        from marketsim.gen._out.strategy.side._Signal import Signal as _strategy_side_Signal
        from marketsim.gen._out._const import const as _const
        from marketsim.gen._out.math._RSI import RSI as _math_RSI
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        return _strategy_Generic(self.orderFactory(_strategy_side_Signal((_const(50.0)-_math_RSI(_orderbook_OfTrader(),self.timeframe,self.alpha)),(50.0-self.threshold))),self.eventGen)
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
