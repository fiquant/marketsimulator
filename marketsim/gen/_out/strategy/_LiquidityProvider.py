from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import ISingleAssetStrategy
from marketsim import Side
from marketsim import registry
from marketsim import IEvent
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "LiquidityProvider"])
class LiquidityProvider_IEventSideFloatIOrderGeneratorFloatFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, eventGen = None, orderFactory = None, initialValue = None, priceDistr = None):
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.event._every import Every_Float as _event_Every
        from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit_IFunctionFloat as _order__curried_sideprice_Limit
        from marketsim.gen._out.math.random._lognormvariate import lognormvariate_FloatFloat as _math_random_lognormvariate
        from marketsim import event
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate
        self.eventGen = eventGen if eventGen is not None else _event_Every(_math_random_expovariate(1.0))
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_sideprice_Limit()
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
        'initialValue' : float,
        'priceDistr' : IFunction[float]
    }
    def __repr__(self):
        return "LiquidityProvider(%(eventGen)s, %(orderFactory)s, %(initialValue)s, %(priceDistr)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy._array import Array_ListISingleAssetStrategy as _strategy_Array
        from marketsim.gen._out.strategy._liquidityproviderside import LiquidityProviderSide_IEventSideFloatIOrderGeneratorSideFloatFloat as _strategy_LiquidityProviderSide
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy
        return _strategy_Array([_strategy_LiquidityProviderSide(self.eventGen,self.orderFactory,_side_Sell(),self.initialValue,self.priceDistr),_strategy_LiquidityProviderSide(self.eventGen,self.orderFactory,_side_Buy(),self.initialValue,self.priceDistr)])
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def LiquidityProvider(eventGen = None,orderFactory = None,initialValue = None,priceDistr = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IEvent
    from marketsim import IOrderGenerator
    from marketsim import Side
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunction[IOrderGenerator,IFunction[Side]
        ,IFunction[float]]):
            if initialValue is None or rtti.can_be_casted(initialValue, float):
                if priceDistr is None or rtti.can_be_casted(priceDistr, IFunction[float]):
                    return LiquidityProvider_IEventSideFloatIOrderGeneratorFloatFloat(eventGen,orderFactory,initialValue,priceDistr)
    raise Exception("Cannot find suitable overload")
