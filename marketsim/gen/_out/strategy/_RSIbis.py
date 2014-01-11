from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim import IEvent
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
from marketsim.gen._out.observable.sidefunc._Signal import Signal as _observable_sidefunc_Signal
from marketsim.gen._out._const import const as _const
from marketsim.gen._out.observable._RSI import RSI as _observable_RSI
from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader as _observable_orderbook_OfTrader
from marketsim import context
@registry.expose(["Strategy", "RSIbis"])
class RSIbis(ISingleAssetStrategy):
    """ 
    """ 
    def __init__(self, eventGen = None, orderFactory = None, alpha = None, timeframe = None, threshold = None):
        from marketsim.gen._out.observable._OnEveryDt import OnEveryDt as _observable_OnEveryDt
        from marketsim.gen._out.order._curried._side_Market import side_Market as _order__curried_side_Market
        from marketsim import event
        from marketsim import _
        self.eventGen = eventGen if eventGen is not None else _observable_OnEveryDt()
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market()
        self.alpha = alpha if alpha is not None else 1.0/14
        self.timeframe = timeframe if timeframe is not None else 1.0
        self.threshold = threshold if threshold is not None else 30.0
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
        'alpha' : float,
        'timeframe' : float,
        'threshold' : float
    }
    def __repr__(self):
        return "RSIbis(%(eventGen)s, %(orderFactory)s, %(alpha)s, %(timeframe)s, %(threshold)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _strategy_Generic(self.orderFactory(_observable_sidefunc_Signal(_const(50.0)-_observable_RSI(_observable_orderbook_OfTrader(),self.timeframe,self.alpha),50.0-self.threshold)),self.eventGen)
    
    
    
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
