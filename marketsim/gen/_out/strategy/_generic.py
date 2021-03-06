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
        self.orderFactory = orderFactory if orderFactory is not None else deref_opt(_order_Limit_SideFloatFloat())
        self.eventGen = eventGen if eventGen is not None else deref_opt(_event_Every_Float())
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
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.orderFactory.bind_ex(self._ctx_ex)
        self.eventGen.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.orderFactory.reset_ex(generation)
        self.eventGen.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._iorder import IOrder
        from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
        from marketsim.gen._out._ievent import IEvent
        rtti.typecheck(IObservableIOrder, self.orderFactory)
        rtti.typecheck(IEvent, self.eventGen)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.orderFactory.registerIn(registry)
        self.eventGen.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.registerIn(registry)
                else:
                    v.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        Generic_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Generic_Impl.reset(self)
    
def Generic(orderFactory = None,eventGen = None): 
    from marketsim.gen._out._iorder import IOrder
    from marketsim.gen._out._iobservable._iobservableiorder import IObservableIOrder
    from marketsim.gen._out._ievent import IEvent
    from marketsim import rtti
    if orderFactory is None or rtti.can_be_casted(orderFactory, IObservableIOrder):
        if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
            return Generic_IObservableIOrderIEvent(orderFactory,eventGen)
    raise Exception('Cannot find suitable overload for Generic('+str(orderFactory) +':'+ str(type(orderFactory))+','+str(eventGen) +':'+ str(type(eventGen))+')')
