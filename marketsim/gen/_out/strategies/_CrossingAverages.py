from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim import IEvent
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim.gen._out.strategies._Generic import Generic as _strategies_Generic
from marketsim.gen._out.observable.sidefunc._CrossingAverages import CrossingAverages as _observable_sidefunc_CrossingAverages
from marketsim import context
@registry.expose(["Strategy", "CrossingAverages"])
class CrossingAverages(ISingleAssetStrategy):
    """  with different parameters ('slow' and 'fast' averages) and when
     the first is greater than the second one it buys,
     when the first is lower than the second one it sells
    """ 
    def __init__(self, eventGen = None, orderFactory = None, ewma_alpha_1 = None, ewma_alpha_2 = None, threshold = None):
        from marketsim.gen._out.observable._OnEveryDt import OnEveryDt as _observable_OnEveryDt
        from marketsim.gen._out.order._curried._side_Market import side_Market as _order__curried_side_Market
        from marketsim import event
        from marketsim import _
        self.eventGen = eventGen if eventGen is not None else _observable_OnEveryDt()
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market()
        self.ewma_alpha_1 = ewma_alpha_1 if ewma_alpha_1 is not None else 0.15
        self.ewma_alpha_2 = ewma_alpha_2 if ewma_alpha_2 is not None else 0.015
        self.threshold = threshold if threshold is not None else 0.0
        self.impl = self.getImpl()
        self.on_order_created = event.Event()
        event.subscribe(self.impl.on_order_created, _(self)._send, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'eventGen' : IEvent,
        'orderFactory' : IFunction[IOrderGenerator,IFunction[Side]]
        
        
        ,
        'ewma_alpha_1' : float,
        'ewma_alpha_2' : float,
        'threshold' : float
    }
    def __repr__(self):
        return "CrossingAverages(%(eventGen)s, %(orderFactory)s, %(ewma_alpha_1)s, %(ewma_alpha_2)s, %(threshold)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _strategies_Generic(self.orderFactory(_observable_sidefunc_CrossingAverages(self.ewma_alpha_1,self.ewma_alpha_2,self.threshold)),self.eventGen)
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
