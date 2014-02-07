from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import ISingleAssetStrategy
from marketsim import Side
from marketsim import registry
from marketsim import IEvent
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "LiquidityProviderSide"])
class LiquidityProviderSide_Optional__IEvent___Optional__________Side__________Float_______IOrderGenerator___Optional________Side___Optional__Float___Optional________Float_(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, eventGen = None, orderFactory = None, side = None, initialValue = None, priceDistr = None):
        from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out.math.random._lognormvariate import lognormvariate as _math_random_lognormvariate
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._sideprice_Limit import sideprice_Limit as _order__curried_sideprice_Limit
        from marketsim import event
        from marketsim.gen._out.event._Every import Every as _event_Every
        self.eventGen = eventGen if eventGen is not None else _event_Every(_math_random_expovariate(1.0))
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_sideprice_Limit()
        self.side = side if side is not None else _side_Sell()
        self.initialValue = initialValue if initialValue is not None else 100.0
        self.priceDistr = priceDistr if priceDistr is not None else _math_random_lognormvariate(0.0,0.1)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'eventGen' : IEvent,
        'orderFactory' : IFunction[IOrderGenerator,IFunction[Side]
        ,IFunction[float]],
        'side' : IFunction[Side],
        'initialValue' : float,
        'priceDistr' : IFunction[float]
    }
    def __repr__(self):
        return "LiquidityProviderSide(%(eventGen)s, %(orderFactory)s, %(side)s, %(initialValue)s, %(priceDistr)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy.price._LiquidityProvider import LiquidityProvider as _strategy_price_LiquidityProvider
        return _strategy_Generic(self.orderFactory(self.side,_strategy_price_LiquidityProvider(self.side,self.initialValue,self.priceDistr)),self.eventGen)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def LiquidityProviderSide(eventGen = None,orderFactory = None,side = None,initialValue = None,priceDistr = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IEvent
    from marketsim import IOrderGenerator
    from marketsim import Side
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunction[IOrderGenerator,IFunction[Side]
        ,IFunction[float]]):
            if side is None or rtti.can_be_casted(side, IFunction[Side]):
                if initialValue is None or rtti.can_be_casted(initialValue, float):
                    if priceDistr is None or rtti.can_be_casted(priceDistr, IFunction[float]):
                        return LiquidityProviderSide_Optional__IEvent___Optional__________Side__________Float_______IOrderGenerator___Optional________Side___Optional__Float___Optional________Float_(eventGen,orderFactory,side,initialValue,priceDistr)
    raise Exception("Cannot find suitable overload")
