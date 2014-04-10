# generated with class generator.python.intrinsic_function$Import
from marketsim import registry
from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
from marketsim.gen._intrinsic.strategy.generic import Generic_Impl
from marketsim.gen._out._iorder import IOrder
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
@registry.expose(["Strategy", "Generic"])
class Generic_IObservableIOrderIEvent(ISingleAssetStrategy,Generic_Impl):
    """ **Generic strategy that wakes up on events given by *eventGen*,**
    
      creates an order via *orderFactory* and sends the order to the market using its trader
    
    Parameters are:
    
    **orderFactory**
    	 order factory function
    
    **eventGen**
    	 Event source making the strategy to wake up
    """ 
    def __init__(self, orderFactory = None, eventGen = None):
        from marketsim.gen._out.order._limit import Limit_SideFloatFloat as _order_Limit_SideFloatFloat
        from marketsim import deref_opt
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim import rtti
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order_Limit_SideFloatFloat())
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float())
        rtti.check_fields(self)
        Generic_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'orderFactory' : IObservableIOrder,
        'eventGen' : IEvent
    }
    
    
    
    
    def __repr__(self):
        return "Generic(%(orderFactory)s, %(eventGen)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_bound_ex'): return
        self._bound_ex = True
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        self._processing_ex = True
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        if hasattr(self, 'bind_impl'): self.bind_impl(self._ctx_ex)
        self.orderFactory.bind_ex(self._ctx_ex)
        self.eventGen.bind_ex(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def Generic(orderFactory = None,eventGen = None): 
    from marketsim.gen._out._iorder import IOrder
    from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
    from marketsim.gen._out._ievent import IEvent
    from marketsim import rtti
    if orderFactory is None or rtti.can_be_casted(orderFactory, IObservableIOrder):
        if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
            return Generic_IObservableIOrderIEvent(orderFactory,eventGen)
    raise Exception('Cannot find suitable overload for Generic('+str(orderFactory) +':'+ str(type(orderFactory))+','+str(eventGen) +':'+ str(type(eventGen))+')')
