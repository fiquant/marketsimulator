from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
@registry.expose(["Strategy", "Noise"])
class Noise_IEventSideIObservableIOrder(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, eventGen = None, orderFactory = None):
        from marketsim import deref_opt
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import event
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float(deref_opt(_math_random_expovariate_Float(1.0))))
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order__curried_side_Market_Float())
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrder_from_IFunctionSide
    }
    def __repr__(self):
        return "Noise(%(eventGen)s, %(orderFactory)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy.side._noise import Noise_Float as _strategy_side_Noise_Float
        from marketsim import deref_opt
        return deref_opt(_strategy_Generic_IObservableIOrderIEvent(deref_opt(self.orderFactory(deref_opt(_strategy_side_Noise_Float()))),self.eventGen))
    
    def __getattr__(self, name):
        if name[0:2] != '__' and self.impl:
            return getattr(self.impl, name)
        else:
            raise AttributeError
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def Noise(eventGen = None,orderFactory = None): 
    from marketsim.gen._out._ievent import IEvent
    from marketsim.gen._out._ifunction._ifunctioniobservableiorder_from_ifunctionside import IFunctionIObservableIOrder_from_IFunctionSide
    from marketsim import rtti
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrder_from_IFunctionSide):
            return Noise_IEventSideIObservableIOrder(eventGen,orderFactory)
    raise Exception('Cannot find suitable overload for Noise('+str(eventGen) +':'+ str(type(eventGen))+','+str(orderFactory) +':'+ str(type(orderFactory))+')')
