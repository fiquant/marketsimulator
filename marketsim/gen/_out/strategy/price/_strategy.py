# generated with class generator.python.strategy$Import
from marketsim import registry
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat import IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
@registry.expose(["Price function", "LiquidityProvider"])
class Strategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrder(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, x = None, eventGen = None, orderFactory = None):
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import rtti
        from marketsim.gen._out.event._event import Event
        from marketsim import _
        from marketsim import event
        from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider_FloatFloatIOrderBook as _strategy_price_LiquidityProvider_FloatFloatIOrderBook
        from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit_Float as _order__curried_sideprice_Limit_Float
        from marketsim import deref_opt
        self.x = x if x is not None else deref_opt(_strategy_price_LiquidityProvider_FloatFloatIOrderBook())
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float(deref_opt(_math_random_expovariate_Float(1.0))))
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_sideprice_Limit_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        
        self.on_order_created = Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : LiquidityProvider,
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
    }
    
    
    
    
    
    
    def __repr__(self):
        return "LiquidityProvider(%(x)s, %(eventGen)s, %(orderFactory)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.x.bind_ex(self._ctx_ex)
        self.eventGen.bind_ex(self._ctx_ex)
        self.orderFactory.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.impl.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.x.reset_ex(generation)
        self.eventGen.reset_ex(generation)
        self.orderFactory.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.impl.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        from marketsim import context
        self.impl = self.getImpl()
        ctx_ex = getattr(self, '_ctx_ex', None)
        if ctx_ex: self.impl.bind_ex(ctx_ex)
        
    
    def getImpl(self):
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.strategy._combine import Combine_ISingleAssetStrategyISingleAssetStrategy as _strategy_Combine_ISingleAssetStrategyISingleAssetStrategy
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        from marketsim.gen._out.strategy.price._onesidestrategy import OneSideStrategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrderSide as _strategy_price_OneSideStrategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrderSide
        from marketsim import deref_opt
        return deref_opt(_strategy_Combine_ISingleAssetStrategyISingleAssetStrategy(deref_opt(_strategy_price_OneSideStrategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrderSide(self.x,self.eventGen,self.orderFactory,deref_opt(_side_Sell_()))),deref_opt(_strategy_price_OneSideStrategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrderSide(self.x,self.eventGen,self.orderFactory,deref_opt(_side_Buy_())))))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    @property
    def suspended(self):
        return self.inner.suspended
    
    def set_suspended(self, value):
        self.inner.suspended = value
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def Strategy(x = None,eventGen = None,orderFactory = None): 
    from marketsim.gen._out.strategy.price._liquidityprovider import LiquidityProvider
    from marketsim.gen._out._ievent import IEvent
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionsideifunctionfloat import IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, LiquidityProvider):
        if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
            if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSideIFunctionfloat):
                return Strategy_strategypriceLiquidityProviderIEventSideFloatIObservableIOrder(x,eventGen,orderFactory)
    raise Exception('Cannot find suitable overload for Strategy('+str(x) +':'+ str(type(x))+','+str(eventGen) +':'+ str(type(eventGen))+','+str(orderFactory) +':'+ str(type(orderFactory))+')')
