from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim import registry
from marketsim import context
@registry.expose(["Strategy", "FundamentalValue"])
class FundamentalValue_IEventSideIObservableIOrderIObservableFloat(ISingleAssetStrategy):
    """  (*fundamental value*) and if the current asset price is lower than the fundamental value
     it starts to buy the asset and if the price is higher it starts to sell the asset.
    """ 
    def __init__(self, eventGen = None, orderFactory = None, fundamentalValue = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import event
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float(deref_opt(_math_random_expovariate_Float(1.0))))
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_side_Market_Float())
        self.fundamentalValue = fundamentalValue if fundamentalValue is not None else deref_opt(_const_Float(100.0))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSide,
        'fundamentalValue' : IObservablefloat
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
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_IObservableFloatIOrderBook as _strategy_side_FundamentalValue_IObservableFloatIOrderBook
        from marketsim import deref_opt
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(self.orderFactory(deref_opt(_strategy_side_FundamentalValue_IObservableFloatIOrderBook(self.fundamentalValue)))),self.eventGen))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
@registry.expose(["Strategy", "FundamentalValue"])
class FundamentalValue_IEventSideIObservableIOrderFloat(ISingleAssetStrategy):
    """  (*fundamental value*) and if the current asset price is lower than the fundamental value
     it starts to buy the asset and if the price is higher it starts to sell the asset.
    """ 
    def __init__(self, eventGen = None, orderFactory = None, fundamentalValue = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import event
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float(deref_opt(_math_random_expovariate_Float(1.0))))
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_side_Market_Float())
        self.fundamentalValue = fundamentalValue if fundamentalValue is not None else deref_opt(_constant_Float(100.0))
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSide,
        'fundamentalValue' : IFunctionfloat
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
        from marketsim.gen._out.strategy._generic import Generic_IObservableIOrderIEvent as _strategy_Generic_IObservableIOrderIEvent
        from marketsim.gen._out.strategy.side._fundamentalvalue import FundamentalValue_FloatIOrderBook as _strategy_side_FundamentalValue_FloatIOrderBook
        from marketsim import deref_opt
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(self.orderFactory(deref_opt(_strategy_side_FundamentalValue_FloatIOrderBook(self.fundamentalValue)))),self.eventGen))
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def FundamentalValue(eventGen = None,orderFactory = None,fundamentalValue = None): 
    from marketsim import rtti
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out._ievent import IEvent
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSide):
            if fundamentalValue is None or rtti.can_be_casted(fundamentalValue, IObservablefloat):
                return FundamentalValue_IEventSideIObservableIOrderIObservableFloat(eventGen,orderFactory,fundamentalValue)
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSide):
            if fundamentalValue is None or rtti.can_be_casted(fundamentalValue, IFunctionfloat):
                return FundamentalValue_IEventSideIObservableIOrderFloat(eventGen,orderFactory,fundamentalValue)
    raise Exception('Cannot find suitable overload for FundamentalValue('+str(eventGen) +':'+ str(type(eventGen))+','+str(orderFactory) +':'+ str(type(orderFactory))+','+str(fundamentalValue) +':'+ str(type(fundamentalValue))+')')
