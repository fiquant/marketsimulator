from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim import IEvent
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
from marketsim.gen._out.observable.sidefunc._MeanReversion import MeanReversion as _observable_sidefunc_MeanReversion
from marketsim import context
@registry.expose(["Strategy", "MeanReversion"])
class MeanReversion(ISingleAssetStrategy):
    """  It estimates this average using some functional and
     if the current asset price is lower than the average
     it buys the asset and if the price is higher it sells the asset.
    """ 
    def __init__(self, eventGen = None, orderFactory = None, ewma_alpha = None):
        from marketsim.gen._out.observable._OnEveryDt import OnEveryDt as _observable_OnEveryDt
        from marketsim.gen._out.order._curried._side_Market import side_Market as _order__curried_side_Market
        from marketsim import event
        from marketsim import _
        self.eventGen = eventGen if eventGen is not None else _observable_OnEveryDt()
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market()
        self.ewma_alpha = ewma_alpha if ewma_alpha is not None else 0.15
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
        'ewma_alpha' : float
    }
    def __repr__(self):
        return "MeanReversion(%(eventGen)s, %(orderFactory)s, %(ewma_alpha)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _strategy_Generic(self.orderFactory(_observable_sidefunc_MeanReversion(self.ewma_alpha)),self.eventGen)
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
