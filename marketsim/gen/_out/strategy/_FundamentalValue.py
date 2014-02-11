from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import ISingleAssetStrategy
from marketsim import Side
from marketsim import registry
from marketsim import IEvent
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "FundamentalValue"])
class FundamentalValue_IEventSideIOrderGeneratorIFunctionFloat(ISingleAssetStrategy):
    """  (*fundamental value*) and if the current asset price is lower than the fundamental value
     it starts to buy the asset and if the price is higher it starts to sell the asset.
    """ 
    def __init__(self, eventGen = None, orderFactory = None, fundamentalValue = None):
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.event._every import Every_Float as _event_Every
        from marketsim import event
        from marketsim.gen._out.order._curried._side_market import side_Market_IFunctionFloat as _order__curried_side_Market
        from marketsim.gen._out._constant import constant_Float as _constant
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate
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
        'orderFactory' : IFunction[IOrderGenerator,IFunction[Side]],
        'fundamentalValue' : IFunction[float]
    }
    def __repr__(self):
        return "FundamentalValue(%(eventGen)s, %(orderFactory)s, %(fundamentalValue)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._generic import Generic_IOrderGeneratorIEvent as _strategy_Generic
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_IFunctionFloatIOrderBook as _strategy_side_FundamentalValue
        return _strategy_Generic(self.orderFactory(_strategy_side_FundamentalValue(self.fundamentalValue)),self.eventGen)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def FundamentalValue(eventGen = None,orderFactory = None,fundamentalValue = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IEvent
    from marketsim import IOrderGenerator
    from marketsim import Side
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunction[IOrderGenerator,IFunction[Side]]):
            if fundamentalValue is None or rtti.can_be_casted(fundamentalValue, IFunction[float]):
                return FundamentalValue_IEventSideIOrderGeneratorIFunctionFloat(eventGen,orderFactory,fundamentalValue)
    raise Exception('Cannot find suitable overload for FundamentalValue('+str(eventGen)+','+str(orderFactory)+','+str(fundamentalValue)+')')
