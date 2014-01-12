from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim import IEvent
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
from marketsim.gen._out.observable.pricefunc._LiquidityProvider import LiquidityProvider as _observable_pricefunc_LiquidityProvider
from marketsim import context
@registry.expose(["Strategy", "LiquidityProviderSide"])
class LiquidityProviderSide(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, eventGen = None, orderFactory = None, side = None, initialValue = None, priceDistr = None):
        from marketsim.gen._out.event._Every import Every as _event_Every
        from marketsim.gen._out.mathutils.rnd._expovariate import expovariate as _mathutils_rnd_expovariate
        from marketsim.gen._out.order._curried._sideprice_Limit import sideprice_Limit as _order__curried_sideprice_Limit
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out.mathutils.rnd._lognormvariate import lognormvariate as _mathutils_rnd_lognormvariate
        from marketsim import event
        from marketsim import _
        self.eventGen = eventGen if eventGen is not None else _event_Every(_mathutils_rnd_expovariate(1.0))
        
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_sideprice_Limit()
        self.side = side if side is not None else _side_Sell()
        self.initialValue = initialValue if initialValue is not None else 100.0
        self.priceDistr = priceDistr if priceDistr is not None else _mathutils_rnd_lognormvariate(0.0,0.1)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'eventGen' : IEvent,
        'orderFactory' : IFunction[IOrderGenerator,IFunction[Side],IFunction[float]]
        
        
        
        ,
        'side' : IFunction[Side]
        ,
        'initialValue' : float,
        'priceDistr' : IFunction[float]
    }
    def __repr__(self):
        return "LiquidityProviderSide(%(eventGen)s, %(orderFactory)s, %(side)s, %(initialValue)s, %(priceDistr)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _strategy_Generic(self.orderFactory(self.side,_observable_pricefunc_LiquidityProvider(self.side,self.initialValue,self.priceDistr)),self.eventGen)
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
