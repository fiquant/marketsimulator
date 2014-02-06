from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import ISingleAssetStrategy
from marketsim import Side
from marketsim import registry
from marketsim import IEvent
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "MeanReversion"])
class MeanReversion_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__Float_(ISingleAssetStrategy):
    """  It estimates this average using some functional and
     if the current asset price is lower than the average
     it buys the asset and if the price is higher it sells the asset.
    """ 
    def __init__(self, eventGen = None, orderFactory = None, ewma_alpha = None):
        from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_Market import side_Market as _order__curried_side_Market
        from marketsim import event
        from marketsim.gen._out.event._Every import Every as _event_Every
        self.eventGen = eventGen if eventGen is not None else _event_Every(_math_random_expovariate(1.0))
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market()
        self.ewma_alpha = ewma_alpha if ewma_alpha is not None else 0.15
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
        'ewma_alpha' : float
    }
    def __repr__(self):
        return "MeanReversion(%(eventGen)s, %(orderFactory)s, %(ewma_alpha)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
        from marketsim.gen._out.strategy.side._MeanReversion import MeanReversion as _strategy_side_MeanReversion
        return _strategy_Generic(self.orderFactory(_strategy_side_MeanReversion(self.ewma_alpha)),self.eventGen)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def MeanReversion(eventGen = None,orderFactory = None,ewma_alpha = None): 
    return MeanReversion_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__Float_(eventGen,orderFactory,ewma_alpha)
