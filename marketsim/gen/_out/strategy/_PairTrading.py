from marketsim.gen._out._ievent import IEvent
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
from marketsim import registry
from marketsim import context
@registry.expose(["Strategy", "PairTrading"])
class PairTrading_IEventSideIObservableIOrderIOrderBookFloat(ISingleAssetStrategy):
    """  is completely correlated with price of another asset *B* and the following relation
     should be held: *PriceA* = *kPriceB*, where *k* is some factor.
     It may be considered as a variety of a fundamental value strategy
     with the exception that it is invoked every the time price of another
     asset *B* changes.
    """ 
    def __init__(self, eventGen = None, orderFactory = None, bookToDependOn = None, factor = None):
        from marketsim import _
        from marketsim import rtti
        from marketsim.gen._out.order._curried._side_market import side_Market_Float as _order__curried_side_Market_Float
        from marketsim.gen._out.orderbook._oftrader import OfTrader_IAccount as _orderbook_OfTrader_IAccount
        from marketsim.gen._out.event._every import Every_Float as _event_Every_Float
        from marketsim.gen._out.math.random._expovariate import expovariate_Float as _math_random_expovariate_Float
        from marketsim import event
        self.eventGen = eventGen if eventGen is not None else _event_Every_Float(_math_random_expovariate_Float(1.0))
        self.orderFactory = orderFactory if orderFactory is not None else _order__curried_side_Market_Float()
        self.bookToDependOn = bookToDependOn if bookToDependOn is not None else _orderbook_OfTrader_IAccount()
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
        'orderFactory' : IFunctionIObservableIOrderIFunctionSide,
        'bookToDependOn' : IOrderBook,
        'factor' : float
    }
    def __repr__(self):
        return "PairTrading(%(eventGen)s, %(orderFactory)s, %(bookToDependOn)s, %(factor)s)" % self.__dict__
    
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
        from marketsim.gen._out.strategy.side._pairtrading import PairTrading_IOrderBookFloatIOrderBook as _strategy_side_PairTrading_IOrderBookFloatIOrderBook
        return _strategy_Generic_IObservableIOrderIEvent(self.orderFactory(_strategy_side_PairTrading_IOrderBookFloatIOrderBook(self.bookToDependOn,self.factor)),self.eventGen)
    
    def _send(self, order, source):
        self.on_order_created.fire(order, self)
    
def PairTrading(eventGen = None,orderFactory = None,bookToDependOn = None,factor = None): 
    from marketsim.gen._out._ievent import IEvent
    from marketsim.gen._out._ifunction._ifunctioniobservableiorderifunctionside import IFunctionIObservableIOrderIFunctionSide
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim import rtti
    if eventGen is None or rtti.can_be_casted(eventGen, IEvent):
        if orderFactory is None or rtti.can_be_casted(orderFactory, IFunctionIObservableIOrderIFunctionSide):
            if bookToDependOn is None or rtti.can_be_casted(bookToDependOn, IOrderBook):
                if factor is None or rtti.can_be_casted(factor, float):
                    return PairTrading_IEventSideIObservableIOrderIOrderBookFloat(eventGen,orderFactory,bookToDependOn,factor)
    raise Exception('Cannot find suitable overload for PairTrading('+str(eventGen) +':'+ str(type(eventGen))+','+str(orderFactory) +':'+ str(type(orderFactory))+','+str(bookToDependOn) +':'+ str(type(bookToDependOn))+','+str(factor) +':'+ str(type(factor))+')')
