from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat import IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
from marketsim import registry
from marketsim import context
@registry.expose(["Strategy", "LiquidityProviderSide"])
class LiquidityProviderSide_IEventSideFloatIObservableIOrderSideFloatFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, eventGen = None, orderFactory = None, side = None, initialValue = None, priceDistr = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.math.random._lognormvariate import lognormvariate_FloatFloat as _math_random_lognormvariate_FloatFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit_Float as _order__curried_sideprice_Limit_Float
        from marketsim import event
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float(deref_opt(_math_random_expovariate_Float(1.0))))
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_sideprice_Limit_Float())
        self.side = side if side is not None else deref_opt(_side_Sell_())
        self.initialValue = initialValue if initialValue is not None else 100.0
        self.priceDistr = priceDistr if priceDistr is not None else deref_opt(_math_random_lognormvariate_FloatFloat(0.0,0.1))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat,
        'side' : IFunctionSide,
        'initialValue' : float,
        'priceDistr' : IFunctionfloat
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
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider_SideFloatFloatIOrderBook as _strategy_price_LiquidityProvider_SideFloatFloatIOrderBook
        from marketsim import deref_opt
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(self.orderFactory(self.side,deref_opt(_strategy_price_LiquidityProvider_SideFloatFloatIOrderBook(self.side,self.initialValue,self.priceDistr)))),self.eventGen))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def LiquidityProviderSide(eventGen = None,orderFactory = None,side = None,initialValue = None,priceDistr = None): 
    from marketsim import rtti
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out._ievent import IEvent
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat import IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionside import IFunctionSide
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat):
            if side is None or rtti.can_be_casted(side, IFunctionSide):
                if initialValue is None or rtti.can_be_casted(initialValue, float):
                    if priceDistr is None or rtti.can_be_casted(priceDistr, IFunctionfloat):
                        return LiquidityProviderSide_IEventSideFloatIObservableIOrderSideFloatFloat(eventGen,orderFactory,side,initialValue,priceDistr)
    raise Exception('Cannot find suitable overload for LiquidityProviderSide('+str(eventGen) +':'+ str(type(eventGen))+','+str(orderFactory) +':'+ str(type(orderFactory))+','+str(side) +':'+ str(type(side))+','+str(initialValue) +':'+ str(type(initialValue))+','+str(priceDistr) +':'+ str(type(priceDistr))+')')
