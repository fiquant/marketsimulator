from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import ISingleAssetStrategy
from marketsim import Side
from marketsim import registry
from marketsim import IEvent
from marketsim import context
from marketsim import float
@registry.expose(["Strategy", "CrossingAverages"])
class CrossingAverages_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__Float___Optional__Float___Optional__Float_(ISingleAssetStrategy):
    """  with different parameters ('slow' and 'fast' averages) and when
     the first is greater than the second one it buys,
     when the first is lower than the second one it sells
    """ 
    def __init__(self, eventGen = None, orderFactory = None, ewma_alpha_1 = None, ewma_alpha_2 = None, threshold = None):
        from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_Market import side_Market as _order__curried_side_Market
        from marketsim import event
        from marketsim.gen._out.event._Every import Every as _event_Every
        self.eventGen = eventGen if eventGen is not None else _event_Every(_math_random_expovariate(1.0))
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market()
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
        'orderFactory' : IFunction[IOrderGenerator,IFunction[Side]],
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
        from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
        from marketsim.gen._out.strategy.side._CrossingAverages import CrossingAverages as _strategy_side_CrossingAverages
        return _strategy_Generic(self.orderFactory(_strategy_side_CrossingAverages(self.ewma_alpha_1,self.ewma_alpha_2,self.threshold)),self.eventGen)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def CrossingAverages(eventGen = None,orderFactory = None,ewma_alpha_1 = None,ewma_alpha_2 = None,threshold = None): 
    from marketsim import IFunction
    from marketsim import rtti
    from marketsim import float
    from marketsim import IEvent
    from marketsim import IOrderGenerator
    from marketsim import Side
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunction[IOrderGenerator,IFunction[Side]]):
            if ewma_alpha_1 is None or rtti.can_be_casted(ewma_alpha_1, float):
                if ewma_alpha_2 is None or rtti.can_be_casted(ewma_alpha_2, float):
                    if threshold is None or rtti.can_be_casted(threshold, float):
                        return CrossingAverages_Optional__IEvent___Optional_________Side______IOrderGenerator___Optional__Float___Optional__Float___Optional__Float_(eventGen,orderFactory,ewma_alpha_1,ewma_alpha_2,threshold)
    raise Exception("Cannot find suitable overload")
