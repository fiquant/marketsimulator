from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionsideifunctionfloat import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
@registry.expose(["Strategy", "LiquidityProvider"])
class LiquidityProvider_IEventSideFloatIObservableIOrderFloatFloat(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, eventGen = None, orderFactory = None, initialValue = None, priceDistr = None):
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.math.random._lognormvariate import lognormvariate_FloatFloat as _math_random_lognormvariate_FloatFloat
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim.gen._out.order._curried._sideprice_limit import sideprice_Limit_Float as _order__curried_sideprice_Limit_Float
        from marketsim import event
        self.eventGen = eventGen if eventGen is not None else _event_Every_Float(_math_random_expovariate_Float(1.0))
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_sideprice_Limit_Float()
        self.initialValue = initialValue if initialValue is not None else 100.0
        self.priceDistr = priceDistr if priceDistr is not None else _math_random_lognormvariate_FloatFloat(0.0,0.1)
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrderIFunctionSideIFunctionfloat,
        'initialValue' : float,
        'priceDistr' : IFunctionfloat
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
        from marketsim.gen._out.strategy._array import Array_ListISingleAssetStrategy as _strategy_Array_ListISingleAssetStrategy
        from marketsim.gen._out.strategy._liquidityproviderside import LiquidityProviderSide_IEventSideFloatIObservableIOrderSideFloatFloat as _strategy_LiquidityProviderSide_IEventSideFloatIObservableIOrderSideFloatFloat
        from marketsim.gen._out.side._sell import Sell_ as _side_Sell_
        from marketsim.gen._out.side._buy import Buy_ as _side_Buy_
        return _strategy_Array_ListISingleAssetStrategy([_strategy_LiquidityProviderSide_IEventSideFloatIObservableIOrderSideFloatFloat(self.eventGen,self.orderFactory,_side_Sell_(),self.initialValue,self.priceDistr),_strategy_LiquidityProviderSide_IEventSideFloatIObservableIOrderSideFloatFloat(self.eventGen,self.orderFactory,_side_Buy_(),self.initialValue,self.priceDistr)])
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def LiquidityProvider(eventGen = None,orderFactory = None,initialValue = None,priceDistr = None): 
    from marketsim.gen._out._ievent import IEvent
    from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionsideifunctionfloat import IFunctionIObservableIOrderIFunctionSideIFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrderIFunctionSideIFunctionfloat):
            if initialValue is None or rtti.can_be_casted(initialValue, float):
                if priceDistr is None or rtti.can_be_casted(priceDistr, IFunctionfloat):
                    return LiquidityProvider_IEventSideFloatIObservableIOrderFloatFloat(eventGen,orderFactory,initialValue,priceDistr)
    raise Exception('Cannot find suitable overload for LiquidityProvider('+str(eventGen) +':'+ str(type(eventGen))+','+str(orderFactory) +':'+ str(type(orderFactory))+','+str(initialValue) +':'+ str(type(initialValue))+','+str(priceDistr) +':'+ str(type(priceDistr))+')')
