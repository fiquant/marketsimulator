from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
@registry.expose(["Strategy", "CrossingAverages"])
class CrossingAverages_IEventSideIObservableIOrderFloatFloatFloat(ISingleAssetStrategy):
    """  with different parameters ('slow' and 'fast' averages) and when
     the first is greater than the second one it buys,
     when the first is lower than the second one it sells
    """ 
    def __init__(self, eventGen = None, orderFactory = None, ewma_alpha_1 = None, ewma_alpha_2 = None, threshold = None):
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import event
        self.eventGen = eventGen if eventGen is not None else _event_Every_Float(_math_random_expovariate_Float(1.0))
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market_Float()
        self.ewma_alpha_1 = ewma_alpha_1 if ewma_alpha_1 is not None else 0.15
        self.ewma_alpha_2 = ewma_alpha_2 if ewma_alpha_2 is not None else 0.015
        self.threshold = threshold if threshold is not None else 0.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'eventGen' : IEvent,
        'orderFactory' : IFunctionIObservableIOrderIFunctionSide,
        'ewma_alpha_1' : float,
        'ewma_alpha_2' : float,
        'threshold' : float
    }
    def __repr__(self):
        return "CrossingAverages(%(eventGen)s, %(orderFactory)s, %(ewma_alpha_1)s, %(ewma_alpha_2)s, %(threshold)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy.side._crossingaverages import CrossingAverages_FloatFloatFloatIOrderBook as _strategy_side_CrossingAverages_FloatFloatFloatIOrderBook
        return _strategy_Generic_IObservableIOrderIEvent(self.orderFactory(_strategy_side_CrossingAverages_FloatFloatFloatIOrderBook(self.ewma_alpha_1,self.ewma_alpha_2,self.threshold)),self.eventGen)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def CrossingAverages(eventGen = None,orderFactory = None,ewma_alpha_1 = None,ewma_alpha_2 = None,threshold = None): 
    from marketsim.gen._out._ievent import IEvent
    from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
    from marketsim import rtti
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrderIFunctionSide):
            if ewma_alpha_1 is None or rtti.can_be_casted(ewma_alpha_1, float):
                if ewma_alpha_2 is None or rtti.can_be_casted(ewma_alpha_2, float):
                    if threshold is None or rtti.can_be_casted(threshold, float):
                        return CrossingAverages_IEventSideIObservableIOrderFloatFloatFloat(eventGen,orderFactory,ewma_alpha_1,ewma_alpha_2,threshold)
    raise Exception('Cannot find suitable overload for CrossingAverages('+str(eventGen) +':'+ str(type(eventGen))+','+str(orderFactory) +':'+ str(type(orderFactory))+','+str(ewma_alpha_1) +':'+ str(type(ewma_alpha_1))+','+str(ewma_alpha_2) +':'+ str(type(ewma_alpha_2))+','+str(threshold) +':'+ str(type(threshold))+')')
