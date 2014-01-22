from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim import IEvent
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
from marketsim.gen._out.strategy.side._FundamentalValue import FundamentalValue as _strategy_side_FundamentalValue
from marketsim import context
@registry.expose(["Strategy", "FundamentalValue"])
class FundamentalValue(ISingleAssetStrategy):
    """  (*fundamental value*) and if the current asset price is lower than the fundamental value
     it starts to buy the asset and if the price is higher it starts to sell the asset.
    """ 
    def __init__(self, eventGen = None, orderFactory = None, fundamentalValue = None):
        from marketsim.gen._out.event._Every import Every as _event_Every
        from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim.gen._out.order._curried._side_Market import side_Market as _order__curried_side_Market
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        from marketsim import event
        from marketsim import _
        self.eventGen = eventGen if eventGen is not None else _event_Every(_math_random_expovariate(1.0))
        
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market()
        self.fundamentalValue = fundamentalValue if fundamentalValue is not None else _constant(100.0)
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
        'fundamentalValue' : IFunction[float]
    }
    def __repr__(self):
        return "FundamentalValue(%(eventGen)s, %(orderFactory)s, %(fundamentalValue)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _strategy_Generic(self.orderFactory(_strategy_side_FundamentalValue(self.fundamentalValue)),self.eventGen)
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
