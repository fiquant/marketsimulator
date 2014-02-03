from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim import IEvent
from marketsim import IEvent
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
from marketsim.gen._out.strategy.side._TrendFollower import TrendFollower as _strategy_side_TrendFollower
from marketsim import context
@registry.expose(["Strategy", "TrendFollower"])
class TrendFollower(ISingleAssetStrategy):
    """  where the *signal* is a trend of the asset.
     Under trend we understand the first derivative of some moving average of asset prices.
     If the derivative is positive, the trader buys; if negative - it sells.
     Since moving average is a continuously changing signal, we check its
     derivative at moments of time given by *eventGen*.
    """ 
    def __init__(self, eventGen = None, orderFactory = None, ewma_alpha = None, threshold = None):
        from marketsim.gen._out.event._Every import Every as _event_Every
        from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim.gen._out.event._Every import Every as _event_Every
        from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim.gen._out.order._curried._side_Market import side_Market as _order__curried_side_Market
        from marketsim.gen._out.order._curried._side_Market import side_Market as _order__curried_side_Market
        from marketsim import rtti
        from marketsim import event
        from marketsim import _
        self.eventGen = eventGen if eventGen is not None else _event_Every(_math_random_expovariate(1.0))
        
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market()
        self.ewma_alpha = ewma_alpha if ewma_alpha is not None else 0.15
        self.threshold = threshold if threshold is not None else 0.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'eventGen' : IEvent,
        'orderFactory' : IFunction[IOrderGenerator,IFunction[Side]]
        
        
        
        
        
        ,
        'ewma_alpha' : float,
        'threshold' : float
    }
    def __repr__(self):
        return "TrendFollower(%(eventGen)s, %(orderFactory)s, %(ewma_alpha)s, %(threshold)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _strategy_Generic(self.orderFactory(_strategy_side_TrendFollower(self.ewma_alpha,self.threshold)),self.eventGen)
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
