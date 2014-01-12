from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim import IEvent
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import Side
from marketsim import IFunction
from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
from marketsim.gen._out.observable.sidefunc._Signal import Signal as _observable_sidefunc_Signal
from marketsim import context
@registry.expose(["Strategy", "Signal"])
class Signal(ISingleAssetStrategy):
    """  and when the signal becomes more than some threshold the strategy starts to buy.
     When the signal gets lower than -threshold the strategy starts to sell.
    """ 
    def __init__(self, eventGen = None, orderFactory = None, signal = None, threshold = None):
        from marketsim.gen._out.event._Every import Every as _event_Every
        from marketsim.gen._out.mathutils.rnd._expovariate import expovariate as _mathutils_rnd_expovariate
        from marketsim.gen._out.order._curried._side_Market import side_Market as _order__curried_side_Market
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import _
        self.eventGen = eventGen if eventGen is not None else _event_Every(_mathutils_rnd_expovariate(1.0))
        
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market()
        self.signal = signal if signal is not None else _constant(0.0)
        self.threshold = threshold if threshold is not None else 0.7
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
        'signal' : IFunction[float],
        'threshold' : float
    }
    def __repr__(self):
        return "Signal(%(eventGen)s, %(orderFactory)s, %(signal)s, %(threshold)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _strategy_Generic(self.orderFactory(_observable_sidefunc_Signal(self.signal,self.threshold)),self.eventGen)
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
