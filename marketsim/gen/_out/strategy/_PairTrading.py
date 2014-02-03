from marketsim import registry
from marketsim import ISingleAssetStrategy
from marketsim import IEvent
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderBook
from marketsim import float
from marketsim import context
@registry.expose(["Strategy", "PairTrading"])
class PairTrading(ISingleAssetStrategy):
    """  is completely correlated with price of another asset *B* and the following relation
     should be held: *PriceA* = *kPriceB*, where *k* is some factor.
     It may be considered as a variety of a fundamental value strategy
     with the exception that it is invoked every the time price of another
     asset *B* changes.
    """ 
    def __init__(self, eventGen = None, orderFactory = None, bookToDependOn = None, factor = None):
        from marketsim.gen._out.event._Every import Every as _event_Every
        from marketsim.gen._out.math.random._expovariate import expovariate as _math_random_expovariate
        from marketsim.gen._out.order._curried._side_Market import side_Market as _order__curried_side_Market
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        from marketsim import rtti
        from marketsim import event
        from marketsim import _
        self.eventGen = eventGen if eventGen is not None else _event_Every(_math_random_expovariate(1.0))
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market()
        self.bookToDependOn = bookToDependOn if bookToDependOn is not None else _orderbook_OfTrader()
        self.factor = factor if factor is not None else 1.0
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
        'bookToDependOn' : IOrderBook,
        'factor' : float
    }
    def __repr__(self):
        return "PairTrading(%(eventGen)s, %(orderFactory)s, %(bookToDependOn)s, %(factor)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.strategy._Generic import Generic as _strategy_Generic
        from marketsim.gen._out.strategy.side._PairTrading import PairTrading as _strategy_side_PairTrading
        return _strategy_Generic(self.orderFactory(_strategy_side_PairTrading(self.bookToDependOn,self.factor)),self.eventGen)
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
